import interactions
from interactions import slash_command
import random

class Dice(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(
        name="dice",
        description="擲骰子"
    )
    async def _dice(self, ctx):
        await ctx.send(f"擲出了 {random.randint(1, 6)} 點")
        
def setup(bot):
    Dice(bot)
