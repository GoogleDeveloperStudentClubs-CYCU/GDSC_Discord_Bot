import discord
from discord.ext import commands, tasks
from discord import app_commands
import random
import aiohttp

class MsgCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.startswith('給我錢') or message.content.endswith('給我錢'):
            await message.add_reaction('\U0001F4B5')
            return
        
    @commands.command()
    async def help(self, ctx):
        await ctx.channel.send(
          '現有指令:\n'
          '> !ELM.meme  : random meme (if not working , just try it again~ )\n '
          '> !ELM.meow  : 吸吸吸吸吸'
          )
        return
    
    @commands.command() # 新增一個叫做 meme 的 command ( message Command )
    async def meme(self, ctx):
        embed = discord.Embed(title="", description="")
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 24)]['data']['url'])
            await ctx.channel.send(embed=embed)
            return
            
    @commands.command() # 新增一個叫做 meow 的 command ( message Command )
    async def meow(self, ctx):     
        embed = discord.Embed(title="", description="")
        url = 'https://www.reddit.com/r/cat/new.json?sort=hot'  # 設定 url
        # 進行爬蟲
        async with aiohttp.ClientSession() as cs:  
          async with cs.get(url) as r:
            res = await r.json()  # 讀取 json 檔
            # 抓取檔案中的 img 網址
            img = res['data']['children'][random.randint(0, 24)]['data']['url']
            # 確認是否為 jpg
            while(not str(img).endswith('.jpg')):
              img = res['data']['children'][random.randint(0, 24)]['data']['url']
              print(img)              
            # 發出訊息
            embed.set_image(url=img)
            await ctx.channel.send(embed=embed)
            return
    
        
async def setup(bot):
    await bot.add_cog(MsgCommands(bot)) # 把 MsgCommands 這個 Cog 加進 bot
