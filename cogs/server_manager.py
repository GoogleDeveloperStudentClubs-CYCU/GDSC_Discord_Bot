import interactions
from interactions import listen
from interactions.api.events import MemberAdd, MessageReactionAdd, MessageReactionRemove, Ready

targetGuildId = 1006577122342600714
targetChannelId = 1010208067142570116
targetMessageId = 1147580972964003901

class ServerManager(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    
    @listen(MemberAdd)
    async def on_member_join(self, memberEvent: MemberAdd):
        guild = memberEvent.guild
        channel = guild.system_channel
        
        await channel.send(f"歡迎 {memberEvent.member.user.mention} 加入 {guild.name} !! 😝😝\n記得到 #身分組選擇 選擇你的身分組~")

    @listen(MessageReactionAdd) # 當新增反應時，給予身分組
    async def on_message_reaction_add(self, reactionAddEvent: MessageReactionAdd):
        messageRefer = interactions.MessageReference.for_message(reactionAddEvent.message)
        # if in dm, return
        if reactionAddEvent.message.guild is None:
            return
        if (messageRefer.message_id == targetMessageId 
                and messageRefer.channel_id == targetChannelId and messageRefer.guild_id == targetGuildId): # 指定訊息
            guild = reactionAddEvent.message.guild
            member = guild.get_member(reactionAddEvent.author.id)
            if reactionAddEvent.emoji.name == "🧝‍♂️": # 根據 emoji 來給予身分組
                role = guild.get_role(1010029791589716048) # 冒險者
                await member.add_role(role)
            elif reactionAddEvent.emoji.name == "🧙‍♂️":
                role = guild.get_role(1010030573823213659) # 宗師
                await member.add_role(role)
            elif reactionAddEvent.emoji.name == "🕵️":
                role = guild.get_role(1010031067048190082) # 友校
                await member.add_role(role)

    @listen(MessageReactionRemove) # 當移除反應時，移除身分組
    async def on_message_reaction_remove(self, reactionRemoveEvent: MessageReactionRemove):
        messageRefer = interactions.MessageReference.for_message(reactionRemoveEvent.message)
        if reactionRemoveEvent.message.guild is None:
            return
        if (messageRefer.message_id == targetMessageId 
                and messageRefer.channel_id == targetChannelId and messageRefer.guild_id == targetGuildId):
            guild = reactionRemoveEvent.message.guild
            member = guild.get_member(reactionRemoveEvent.author.id)
            if reactionRemoveEvent.emoji.name == "🧝‍♂️":
                role = guild.get_role(1010029791589716048)
                await member.remove_role(role)
            elif reactionRemoveEvent.emoji.name == "🧙‍♂️":
                role = guild.get_role(1010030573823213659)
                await member.remove_role(role)
            elif reactionRemoveEvent.emoji.name == "🕵️":
                role = guild.get_role(1010031067048190082)
                await member.remove_role(role)


def setup(bot):
    ServerManager(bot)