import interactions
import logging
import pkgutil

def read_token_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

intents = interactions.Intents.ALL
logging.basicConfig()
logger = logging.getLogger("")
logger.setLevel(logging.INFO)
bot = interactions.Client(intents=intents, logger=logger)
  
# 當 bot 完全準備好了以後觸發
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}", flush=True)

# 啟動 bot
bot_token = read_token_from_file("token.txt")
if __name__ == "__main__":
    extensions = [x.name for x in pkgutil.iter_modules(["cogs"], prefix="cogs.")] # 取得 cogs 資料夾下所有的檔案名稱
    for extension in extensions: # 載入所有的擴充功能
        print(f"Loading extension {extension}", flush=True)
        bot.load_extension(extension)
    bot.start(bot_token)


