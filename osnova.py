import discord
from discord.ext import commands
from discord.utils import get

intents = discord.Intents().all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(stx):
    await stx.send('pong')
@bot.command()
async def poshel(stx):
    await stx.send('nahuy')

@bot.command()
async def give(ctx,rolename, member: discord.Member = None):
    if member is None:
        member = ctx.author
    role = get(ctx.guild.roles, name=rolename)
    await member.add_roles(role)
    await ctx.send(f'Роль {rolename} выдана {member}')

bot.run('MTIzMjQwODgwNTkzNDEwODg4NQ.GlSw9Z.l2oB37atqjZN9uMEUman1DJ-rb4rbB91QpfSiA')