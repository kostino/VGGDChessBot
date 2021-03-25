from tournament import Tournament
from discord.ext.commands import Bot

# write here your description and your command_prefix
client = Bot(description="Chess Bot For SeraMG Invitational", command_prefix="!", pm_help=True)


@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def addMatch(ctx):
    await ctx.send("Write White's name")
    white = await client.wait_for('message')
    await ctx.send("Write Black's name")
    black = await client.wait_for('message')
    await ctx.send("Write Result")
    result = await client.wait_for('message')
    players = ['Kostino', 'Mesleh', 'Giannos', 'Hackerman', 'Kooustas', 'Billkapa', 'Aboosker']
    tour = Tournament(players)
    tour.addMatch(white.content, black.content, result.content)
    tour.saveMatches()
    pass

"""
@client.command()
async def saveMatches(ctx):
    players = ['Kostino', 'Mesleh', 'Giannos', 'Hackerman', 'Kooustas', 'Billkapa', 'Aboosker']
    tour = Tournament(players)
    tour.saveMatches()
    pass
"""



@client.command()
async def printTable(ctx):
    players = ['Kostino', 'Mesleh', 'Giannos', 'Hackerman', 'Kooustas', 'Billkapa', 'Aboosker']
    tour = Tournament(players)
    await ctx.send(tour.prettyRanking())


@client.command()
async def printMatchList(ctx):
    players = ['Kostino', 'Mesleh', 'Giannos', 'Hackerman', 'Kooustas', 'Billkapa', 'Aboosker']
    tour = Tournament(players)
    await ctx.send(tour.prettyMatchlist())


# write here your discord bot token
client.run('___YOUR TOKEN___')

