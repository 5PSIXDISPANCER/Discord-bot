import discord
from discord.ext import commands
from discord.utils import get

TOKEN = 'MTIzMjQwODgwNTkzNDEwODg4NQ.GlSw9Z.l2oB37atqjZN9uMEUman1DJ-rb4rbB91QpfSiA'
PREFIX = '!'
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.command()
async def ping(stx):
    await stx.send('pong')

@bot.command()
async def poshel(stx):
    await stx.send('nahuy')

@bot.command()
async def cc(ctx):
    member = ctx.author
    guild = ctx.guild
    role = guild.get_role(1232416938404085910)
    await member.add_roles(role)
bot.run(TOKEN)