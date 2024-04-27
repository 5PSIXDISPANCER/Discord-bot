import discord
import config
from discord.ext import commands
from discord.utils import get

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=config.prefix, intents=intents)


@bot.command()
async def ping2(stx):
    await stx.send('pong')