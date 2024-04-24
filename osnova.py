import discord
import config
from discord.ext import commands
from discord.utils import get

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=config.prefix, intents=intents)

@bot.command()
async def ping(stx):
    await stx.send('pong')
@bot.command()
async def poshel(stx):
    await stx.send('nahuy')

@bot.command()
async def give(ctx):
    member = ctx.author
    guild = ctx.guild
    role = guild.get_role(1232416938404085910)
    await member.add_roles(role)

@bot.event
async def on_message(ctx):
    member = ctx.author
    guild = ctx.guild
    role = guild.get_role(config.token_role_nigger)
    await member.add_roles(role)

# Снятие ролей 
@bot.command()
async def b(ctx):
    member = ctx.author
    guild = ctx.guild
    role = guild.get_role(config.token_role_nigger)
    await member.remove_roles(role)



bot.run(config.token)