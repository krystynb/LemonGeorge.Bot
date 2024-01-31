import os
import discord
import random
from discord.ext import commands, tasks
from dotenv import load_dotenv
load_dotenv()
import yt_dlp as youtube_dl 

# retrieve bot token and guild name from .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#set intents for the bot so it has access to everything
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='`', intents =intents)

#print what guilds the bot is in, info about all the guild members, loads the cogs
@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([f"{member.name} (ID: {member.id})" for member in guild.members])
    print(f'Guild Members:\n - {members}')
    
    try:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"cogs.{filename[:-3]} Loaded!")
    except commands.ExtensionError as e:
        print(f"Failed to load cog: {e}") 
    
#send a welcome DM from the bot 
@bot.event
async def on_member_join(member):
    await member.create_dm()
    try:
        await member.dm_channel.send(f'Hi {member.name}, welcome to the milk jug!')
        print(f"Sent welcome message to {member.name}")
    except discord.errors.Forbidden:
        print(f"Could not send a welcome message to {member.name}. Missing permissions or DMs disabled.")
    except Exception as e:
        print(f"An error occurred while sending a welcome message to {member.name}: {e}")
            
bot.run(TOKEN)
