import discord
from discord.ext import commands, tasks
from discord import app_commands
import random
import aiohttp

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command() # 新增一個叫做 meme 的 command ( message Command )
    async def meme(self, ctx):
        embed = discord.Embed(title="", description="")
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 24)]['data']['url'])
            await ctx.channel.send(embed=embed)
            return
        
async def setup(bot):
    await bot.add_cog(Meme(bot)) # 把 Meme 這個 Cog 加進 bot
