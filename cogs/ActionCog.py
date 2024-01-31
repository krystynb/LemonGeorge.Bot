from discord.ext import commands
import random
from .botMsgs import maps

class ActionCog(commands.Cog, name='Actions'):
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name='roll-dice', help="specify the number of dice and number of sides to roll dice")
    async def roll(self, ctx, numDice: int, numSides: int):
        dice = [
            f'die {x + 1}: {random.choice(range(1, numSides + 1))}\n'
            for x in range(numDice)
        ]
        await ctx.channel.send(''.join(dice))

async def setup(bot):
    await bot.add_cog(ActionCog(bot))