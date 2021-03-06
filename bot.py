import discord
import os
from discord.ext import commands
import config

TOKEN = config.TOKEN
PREFIX = config.PREFIX
STATUS = config.STATUS
OWNER_UID = config.OWNER_UID
GUILD_UID = config.GUILD_UID


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game(STATUS)
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def load(ctx, extension):
    if ctx.message.author.id != OWNER_UID:
        return 
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    if ctx.message.author.id != OWNER_UID:
        return 
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)