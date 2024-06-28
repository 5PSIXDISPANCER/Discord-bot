import disnake
# import pytube
from asyncio import sleep
import config

from db import *
import datetime
from openpyxl import Workbook
from dpyConsole import Console
from disnake.ui import Button, View
from discord_webhook import DiscordWebhook, DiscordEmbed 
from disnake.voice_client import VoiceClient
from disnake.ext import commands 
from disnake.utils import get 


#Переменные необходимые в коде, для его сокращения.
intents = disnake.Intents().all() #разрешения
bot = commands.Bot(command_prefix=config.prefix, intents=intents) #префикс команд и разрешения
my_console = Console(bot)

@bot.event
async def on_guild_join(guild: disnake.Guild):
    print(f'Bee прилетел на {guild.name}')
    await db_add_guild(guild)

# @my_console.command()
# async def resdb():
#     print('Are you sure? Y/N')
#     a = await input().lower()
#     if a == 'y':
#         print('DB reset starting')
#         await dblogging(bot)   
#логирование сообщений, первая часть кода логирует в файл в более краткой форме, вторая часть логирует в файл и в #log
async def log(message: disnake.Message):
    now = datetime.datetime.now()
    if message.attachments:
        for i in range(len(message.attachments)):
            with open('log.txt', 'a') as file:
                 file.write(f'{now.strftime("%H:%M:%S")} {message.author.name}: {message.attachments[i]}\n')      
    else:
        with open('log.txt', 'a') as file:
             file.write(f"Дата: {now.strftime("%d/%m/%Y")} Время: {now.strftime("%H:%M:%S")} Автор: {message.author} ({message.author.id}) Категория: {message.channel.category} ({message.channel.category.id}) Канал: {message.channel} ({message.channel.id}) Сообщение: {message.content}\n")
        log_webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1242202771294261429/kch_F1G9r3k9SdQn1LzpOQtr4fSyuc9ZpAYfE_ad5GWPthLVXSCfIh8xhf_CUx8o-DIo')
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
async def on_message(message: disnake.Message):
    if message.webhook_id is not None:
        return
    await bot.process_commands(message)
    await log(message)
    await db_add_exp(message)


@bot.command()
async def exp(ctx):
    response = await db_get_exp(ctx)
    await ctx.send(f'У {ctx.author.mention} {response} exp')

@bot.command()
async def logs(ctx):
    await ctx.send(file=disnake.File(r'log.txt'))

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
    await stx.send(file = disnake.File(r'parser.xlsx'))

@bot.command(description="Sends the bot's latency.")
async def poshel(stx):
    await stx.send(bot.guilds[0].members[0].default_avatar)

# Выдать роль
@bot.command()
async def give(ctx,rolename, member: disnake.Member = None):
    if member is None:
        member = ctx.author
    role = get(ctx.guild.roles, name=rolename)
    await member.add_roles(role)
    await ctx.send(f'Роль {rolename} выдана {member.global_name}')

# Убрать роль
@bot.command()
async def remove(ctx, rolename, member: disnake.Member = None):
    if member is None:
        member = ctx.author
    role = get(ctx.guild.roles, name=rolename)
    await member.remove_roles(role)
    await ctx.send(f'Роль {rolename} убрана у {member.global_name}')
    
#удаление сообщений посредством ввода аргумента как число, так и слова все или алл как угодно  
@bot.command()
async def delete(ctx, content):
        if content.isdigit() == True:   
            content = int(content)
            await ctx.channel.purge(limit=content)
            await ctx.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(ctx.author.mention))
            await sleep(3)
            await ctx.channel.purge(limit=1)
        elif content.isalpha():
              content = str(content.lower())
              if content == "all" or content == "все":
                await ctx.channel.purge(limit=100)
                await ctx.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(ctx.author.mention))
                await sleep(3)
                await ctx.channel.purge(limit=1)    

@bot.command()
async def fff(stx, member: disnake.Member = None):
    embedfff = disnake.Embed(title='Игра началась, дети поставлены, ставок БОЛЬШЕ НЕТ!', description='fff')
    embedfff.add_field(name='1 player', value=f'{stx.author}')
    embedfff.add_field(name='2 player', value=f'{member}')
    buttonStone = Button(label='Камень', style=disnake.ButtonStyle.primary)
    buttonScissors = Button(label='Ножницы', style=disnake.ButtonStyle.primary)
    buttonPaper = Button(label='Бумага', style=disnake.ButtonStyle.primary)
    view = View()
    view.add_item(buttonStone)
    view.add_item(buttonScissors)
    view.add_item(buttonPaper)
    await stx.send(embed=embedfff)
    await stx.send(view=view)
    
@bot.slash_command(name ='ебатьслешкоманда')
async def ebat(ctx):
    await ctx.send('Да я сам охуел')

my_console.start()
bot.run(config.token)