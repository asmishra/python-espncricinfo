import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from getTeamLists import GetTeamLists

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='!')

# @bot.event
# async def on_ready():
#     print(f'{bot.user.name} has connected to Discord!')
#     try:
#         synced = await bot.tree.sync()
#         print('Synced {} command(s)'.format(len(synced)))
#     except Exception as e:
#         print(e)


# @bot.tree.command(name='test')
# async def test(interaction: discord.Interaction):
#     await interaction.response.send_message('ZZZ')

# @bot.tree.command(name='hello')
# async def hello(interaction: discord.Interaction):
#     await interaction.response.send_message('ZZZ')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='teams', help='Lists the playing XIs for each team in the list')
async def teams(ctx, *args):
    response = GetTeamLists(args).run()
    await ctx.send(response)


@bot.command(name='whoisplaying', help='Lists the matches currently listed online')
async def whoisplaying(ctx, *args):
    responseList = GetTeamLists([]).getCurrentMatches()
    for partialResponse in responseList:
        await ctx.send(partialResponse)

my_secret = os.environ['DISCORD_TOKEN']
bot.run(my_secret)
