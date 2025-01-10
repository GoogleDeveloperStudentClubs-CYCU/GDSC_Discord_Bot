import interactions
from interactions import slash_command, listen, SlashContext
from interactions.api.events import MessageCreate
import random
import aiohttp

class MsgCommands(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
        
    @listen(MessageCreate)
    async def on_message(self, messageEvent: MessageCreate):
        if messageEvent.message.author == self.bot.user:
            return
        if messageEvent.message.content.startswith('給我錢') or messageEvent.message.content.endswith('給我錢'):
            await messageEvent.message.add_reaction('\U0001F4B5')
            return
        
    @slash_command(name = "help", description="顯示指令使用說明")
    async def help(self, ctx: SlashContext):
        await ctx.send(
          '現有指令:\n'
          '> /meme  : random meme (if not working , just try it again~ )\n '
          '> /meow  : 吸吸吸吸吸'
          )
        return
    
    @slash_command(name = "meme", description="傳送一則 meme") # 新增一個叫做 meme 的 command ( message Command )
    async def meme(self, ctx: SlashContext):
        embed = interactions.Embed(title="", description="")
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 24)]['data']['url'])
            await ctx.send(embeds=embed)
            return
            
    @slash_command(name = "meow", description="傳送一隻貓") # 新增一個叫做 meow 的 command ( message Command )
    async def meow(self, ctx):
        await ctx.defer()  # 延遲回應
        embed = interactions.Embed(title="", description="")
        url = 'https://www.reddit.com/r/cat/new.json?sort=hot'  # 設定 url
        # 進行爬蟲
        async with aiohttp.ClientSession() as cs:  
          async with cs.get(url) as r:
            res = await r.json()  # 讀取 json 檔
            # 抓取檔案中的 img 網址
            img = res['data']['children'][random.randint(0, 24)]['data']['url']
            # 確認是否為 jpg or jpeg
            while(not str(img).endswith('.jpg') and not str(img).endswith('.jpeg')):
              img = res['data']['children'][random.randint(0, 24)]['data']['url']
              # print(img)              
            # 發出訊息
            embed.set_image(url=img)
            await ctx.send(embeds=embed)
            return
    
        
def setup(bot):
    MsgCommands(bot)    
