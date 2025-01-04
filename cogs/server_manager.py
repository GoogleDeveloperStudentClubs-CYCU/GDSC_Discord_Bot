import interactions
from interactions import listen
from interactions.api.events import MemberAdd, MessageReactionAdd, MessageReactionRemove

class ServerManager(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    
    @listen(MemberAdd)
    async def on_member_join(self, member: interactions.Member):
        guild = member.guild
        channel = guild.system_channel
        
        await channel.send(f"歡迎 {member.member.user.mention} 加入 {guild.name} !! 😝😝\n記得到 #身分組選擇 選擇你的身分組~")
            


def setup(bot):
    ServerManager(bot)