from tournament import Tournament
from discord.ext.commands import Bot
from dotenv import load_dotenv
from os import getenv
from os.path import isfile


active_tournament = None
load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

# write here your description and your command_prefix
client = Bot(description="Chess Bot For SeraMG Invitational", command_prefix="~~", pm_help=True)


@client.event
async def on_ready():
    print("ChessBot is ready")


@client.command(name='info')
async def info(ctx):
    await ctx.send("``Active tournament:" + active_tournament.name +'``')


@client.command(name='active')
async def activateTour(ctx, name):
    global active_tournament
    if not isfile(name+'_players.txt'):
        await ctx.send("Tournament doesn't exist")
    active_tournament = Tournament(name)
    await ctx.send("``Active tournament:" + name+'``')


@client.command(name='new_tournament')
async def new(ctx, *args):
    if len(args) < 2:
        await ctx.send("``Usage: ~~new_tournament <name> <player1> <player2> ... ``")
    name = args[0]
    players = args[1:]
    print(players)
    new_tournament = Tournament(name, players)
    new_tournament.save()
    await ctx.send("``Tournament Added:\n" + name + "``")


@client.command(name='add')
async def addMatch(ctx, white, black, result):
    active_tournament.addMatch(white, black, result)
    active_tournament.save()
    await ctx.send("``Match Added:\n" + white + " " + result + " " + black + "``")


"""
@client.command()
async def saveMatches(ctx):
    players = ['Kostino', 'Mesleh', 'Giannos', 'Hackerman', 'Kooustas', 'Billkapa', 'Aboosker']
    tour = Tournament(players)
    tour.saveMatches()
    pass
"""


@client.command(name='ranking')
async def printTable(ctx):
    await ctx.send("``" + active_tournament.prettyRanking() + "``")


@client.command(name='matches')
async def printMatchList(ctx):
    await ctx.send("``" + active_tournament.prettyMatchlist() + "``")


@client.command(name='results')
async def printResults(ctx):
    await ctx.send("``" + active_tournament.prettyResults() + "``")


# write here your discord bot token
client.run(TOKEN)

