import discord
import pytube

import config

from discord.voice_client import VoiceClient
from discord.ext import commands
from discord.utils import get

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=config.prefix, intents=intents)

@bot.command()
async def ping(stx):
    await stx.send(bot.guilds)
    await stx.send(len(bot.guilds[0].members))
    for i in range(len(bot.guilds)):
        await stx.send(f'Сервер {bot.guilds[i]} на нем находятся:')
        for x in range(len(bot.guilds[i].members)):
            await stx.send(bot.guilds[i].members[x].name)
@bot.command()
async def poshel(stx):
    await stx.send('nahuy')

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
async def remove(ctx,rolename, member: discord.Member = None):
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

bot.run(config.token)