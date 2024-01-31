from discord.ext import commands
import random
from .botMsgs import words

class QuestionsCog(commands.Cog, name='Questions'):
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name='hungry?', help='ask LemonGeorge if he\'s hungry')
    async def hungry(self, ctx):
        response = random.choice(words.hungry)
        await ctx.channel.send(response)
    
    @commands.command(name='wyd?', help='ask LemonGeorge what he\'s up to')
    async def wyd(self, ctx):
        response = random.choice(words.wyd)
        await ctx.channel.send(response)
        
    @commands.command(name='seth?', help='ask LemonGeorge what he thinks of seth')
    async def seth(self, ctx):
        response = random.choice(words.seth)
        await ctx.channel.send(response)
        
        
async def setup(bot):
    await bot.add_cog(QuestionsCog(bot))
