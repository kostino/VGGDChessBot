from discord.ext.commands import Bot

# write here your description and your command_prefix
client = Bot(description="Chess Bot For SeraMG Invitational", command_prefix=">", pm_help=True)


@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def hello(ctx):
    await ctx.send("hi")

# write here your discord bot token
client.run('___YOUR TOKEN___')
