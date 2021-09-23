import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in")

    async def on_message(self, message):
        prefix = ">>>"

        if message.content.startswith(prefix + "rpc "):
            rpc = str(message.content)
            rpc = rpc.split(prefix + "rpc ", 1)[1]
            if "p " in rpc:
                rpc = rpc.replace('p ', '')
                await ctx.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=rpc))
                await message.reply("Updated Discord RPC to playing " + rpc, mention_author=False)
            if "l " in rpc:
                rpc = rpc.replace('l ', '')
                await ctx.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=rpc))
                await message.reply("Updated Discord RPC to listening to " + rpc, mention_author=False)
            if "w " in rpc:
                rpc = rpc.replace('w ', '')
                await ctx.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=rpc))
                await message.reply("Updated Discord RPC to watching " + rpc, mention_author=False)


ctx = MyClient()
ctx.run("Your Discord-Token goes here", bot=False)


