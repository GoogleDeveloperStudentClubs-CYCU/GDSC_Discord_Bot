import discord
from discord.ext import commands, tasks

def read_token_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 當 bot 完全準備好了以後觸發
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# 當有新成員加入時觸發
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')  # 你可以修改這裡以選擇其他頻道
    if channel:
        buttons = [
            discord.Button(label='身份組 1', style=discord.ButtonStyle.primary, custom_id='role_1'),
            discord.Button(label='身份組 2', style=discord.ButtonStyle.primary, custom_id='role_2')
        ]
        action_row = discord.ActionRow(*buttons)
        await channel.send(f"歡迎 {member.mention}，請選擇你的身份組。", components=[action_row])

# 處理按鈕事件
@bot.event
async def on_button_click(interaction):
    if interaction.custom_id == 'role_1':
        role = discord.utils.get(interaction.guild.roles, name='Role1')  # 換成你的身份組名稱
    elif interaction.custom_id == 'role_2':
        role = discord.utils.get(interaction.guild.roles, name='Role2')  # 換成你的身份組名稱

    if role:
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"你已經被分配到 {role.name} 身份組！", ephemeral=True)

# 啟動 bot
bot_token = read_token_from_file("token.txt")  # 讀取 token
bot.run(bot_token)
