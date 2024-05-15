import discord
import pytube
import openpyxl

import config

from datetime import datetime
from openpyxl import Workbook
from discord.voice_client import VoiceClient
from discord.ext import commands
from discord.utils import get

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=config.prefix, intents=intents)

async def log(message):
    with open('log.txt', 'a') as file:
        file.write(f'{datetime.now().strftime("%H:%M:%S")} {message.author.name}: {message.content}\n')
        file.close()

@bot.event
async def on_message(message: discord.Message):
    await bot.process_commands(message)
    await log(message)

@bot.command()
async def logs(ctx):
    await ctx.send(file=discord.File(r'log.txt'))

@bot.command()
async def ping(stx):
    book = Workbook()
    sheep = book.active
    mainRow = 1

    for i in range(len(bot.guilds)):
        sheep.cell(row = mainRow, column = 1, value = bot.guilds[i].name)
        for x in range(len(bot.guilds[i].members)):
            sheep.cell(row = mainRow, column = 2, value = bot.guilds[i].members[x].name)
            sheep.cell(row = mainRow, column = 3, value = bot.guilds[i].members[x].global_name)
            if bot.guilds[i].members[x].avatar == None:
                sheep.cell(row = mainRow, column = 4, value = bot.guilds[i].members[x].default_avatar.url)
            else:
                sheep.cell(row = mainRow, column = 4, value = bot.guilds[i].members[x].avatar.url)
            mainRow += 1
    book.save('parser.xlsx')
    book.close
    await stx.send(file = discord.File(r'parser.xlsx'))

@bot.command()
async def poshel(stx):
    await stx.send(bot.guilds[0].members[0].default_avatar)

# Выдать роль
@bot.command()
async def give(ctx,rolename, member: discord.Member = None):
    if member is None:
        member = ctx.author
    role = get(ctx.guild.roles, name=rolename)
    await member.add_roles(role)
    await ctx.send(f'Роль {rolename} выдана {member.global_name}')

# Убрать роль
@bot.command()
async def remove(ctx, rolename, member: discord.Member = None):
    if member is None:
        member = ctx.author
    role = get(ctx.guild.roles, name=rolename)
    await member.remove_roles(role)
    await ctx.send(f'Роль {rolename} убрана у {member.global_name}')
# Доработать
# @bot.command()
# async def play(ctx, yt):
#     if ctx.author.voice is None:
#         await ctx.send('Зайдите в войс канал и попробуйте снова')
#         return
#     yt = pytube.YouTube(yt)
#     stream = yt.streams.filter(only_audio=True).first().download()
#     await ctx.send(f"Видео успешно загружено! {yt}")
#     channel = ctx.message.author.voice.channel
#     await channel.connect()

# @bot.event
# async def on_ready():

@bot.command()
async def gel(ctx, amount = 100):
     await ctx.channel.purge(limit = amount)

@bot.event
async def on_ready():
    channel = bot.get_channel(1233749922893922335)
    members = bot.get_user(701855944384053348)
    await channel.send(members)
bot.run(config.token)