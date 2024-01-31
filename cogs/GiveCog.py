from discord.ext import commands
import random
from .botMsgs import words
from .botMsgs import maps

class GiveCog(commands.Cog, name='Give'):
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name='feed', help='feed LemonGeorge his favorite foods!')
    async def feed(self, ctx, *, args):
        if args in maps.food:
                response = maps.food[args]
        else:
            response = random.choice(words.gross)
        await ctx.channel.send(response)

async def setup(bot):
    await bot.add_cog(GiveCog(bot))