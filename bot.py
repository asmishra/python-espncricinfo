import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from getTeamLists import GetTeamLists

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='teams', help='Lists the playing XIs for each team in the list')
async def teams(ctx, *args):
    response = GetTeamLists(args).run()
    await ctx.send(response)

my_secret = os.environ['DISCORD_TOKEN']
bot.run(my_secret)
