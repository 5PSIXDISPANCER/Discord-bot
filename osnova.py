import discord
# import pytube
import openpyxl

import config

from datetime import datetime #для времени
from openpyxl import Workbook #для логов
from discord_webhook import DiscordWebhook, DiscordEmbed #для логов
from discord.voice_client import VoiceClient
from discord.ext import commands #импорт bot.command()
from discord.utils import get #импорт get

#Переменные необходимые в коде, для его сокращения.
intents = discord.Intents().all() #разрешения
bot = commands.Bot(command_prefix=config.prefix, intents=intents) #префикс команд и разрешения
now = datetime.now() #время и дата

#логирование сообщений, первая часть кода логирует в файл в более краткой форме, вторая часть логирует в файл и в #log
async def log(message: discord.Message):
    if message.attachments:
        for i in range(len(message.attachments)):
            with open('log.txt', 'a') as file:
                 file.write(f'{now.strftime("%H:%M:%S")} {message.author.name}: {message.attachments[i]}\n')
                
    else:
        with open('log.txt', 'a') as file:
             file.write(f"Дата: {now.strftime("%d/%m/%Y")} Время: {now.strftime("%H:%M:%S")} Автор: {message.author} ({message.author.id}) Категория: {message.channel.category} ({message.channel.category.id}) Канал: {message.channel} ({message.channel.id}) Сообщение: {message.content}\n")
        log_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1242202771294261429/kch_F1G9r3k9SdQn1LzpOQtr4fSyuc9ZpAYfE_ad5GWPthLVXSCfIh8xhf_CUx8o-DIo")
        log_embed = DiscordEmbed()
        log_embed.set_author(name= message.author.global_name,  icon_url=message.author.avatar.url)
        log_embed.set_title(title='Сообщение')
        log_embed.set_description(description = message.content)
        log_embed.add_embed_field(name = 'Пользователь и его ID', value = f'{message.author.mention} ( {message.author.id} )', inline = False)
        log_embed.add_embed_field(name = 'Дата', value = f'{now.strftime("%d/%m/%Y")}')
        log_embed.add_embed_field(name = 'Время', value = f'{now.strftime("%H:%M:%S")}', inline=False)
        log_embed.add_embed_field(name = 'Категория и её ID', value = f'{message.channel.category} ( {message.channel.category.id} )', inline=False)
        log_embed.add_embed_field(name = 'Канал и его ID', value = f'{message.channel.mention} ( {message.channel.id} )')
        log_embed.add_embed_field(name = 'Ссылка на сообщение', value = f'{message.jump_url}', inline=False)
        log_webhook.add_embed(log_embed)
        response = log_webhook.execute()


@bot.event
async def on_message(message: discord.Message):
    if message.webhook_id is not None:
        return
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


bot.run(config.token)