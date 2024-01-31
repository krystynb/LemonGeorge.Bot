from discord.ext import commands
from .botMsgs import maps

class FaveCog(commands.Cog, name='Favorite Things'):
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name='favefood', help="list LemonGeorge's favorite foods")
    async def favefood(self, ctx):
        response = "These are my favorite foods: \n"
        for x in maps.food:
            response += ('- ' + x + '\n')
        await ctx.channel.send(response)

async def setup(bot):
    await bot.add_cog(FaveCog(bot))