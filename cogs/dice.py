import discord
from discord.ext import commands, tasks
from discord import app_commands
import random

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name = "dice") # 新增一個叫做 dice 的 Application command (Slash Command) 
    async def dice(self, ctx):
        await ctx.response.send_message(str(random.randint(1,6)))
        
async def setup(bot):
    await bot.add_cog(Dice(bot)) # 把 Dice 這個 Cog 加進 bot
