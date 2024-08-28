import disnake
# import pytube
from asyncio import sleep

import disnake.ext.commands
import config
import for_games
from db import *
import datetime
from typing import Optional
from openpyxl import Workbook
from dpyConsole import Console
from disnake.ui import Button, View
from discord_webhook import DiscordWebhook
from disnake import Embed 
from disnake.voice_client import VoiceClient
from disnake.ext import commands 
from disnake.utils import get

import disnake.ext 


#Переменные необходимые в коде, для его сокращения.
intents = disnake.Intents().all() #разрешения
bot = commands.Bot(command_prefix=config.prefix, intents=intents, test_guilds=[1232407034108973186]) #префикс команд и разрешения
my_console = Console(bot)

@bot.event
async def on_guild_join(guild: disnake.Guild):
    await db_add_guild(guild)


        
class ExpEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def exp(self, stx: disnake.ext.commands.context.Context):
        # response = await db_get_exp(stx)
        # embed = disnake.Embed(
        #     description = f"Количество опыта: {response}",
        #     color = disnake.Colour.yellow(),
        #     timestamp = datetime.datetime.now()
        # )
        # embed.set_author(
        #     name = stx.author.global_name,
        #     icon_url = stx.author.avatar.url
        # )
        # await stx.send(embed=embed)
        await stx.send("Привет")
    
class MiniGames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #проверку чтоб бота не звали сделать 
    @commands.command()
    async def fff(self, stx: disnake.ext.commands.context.Context, member: disnake.member.Member = None):
        # if hasattr(member, 'bot'):
        #     await stx.send('Bee не хочет играть')
        #     return
        embedfff = disnake.Embed(title='Игра началась, дети поставлены, ставок БОЛЬШЕ НЕТ!')
        embedfff.add_field(name='1 player', value=f'{stx.author.global_name}')
        if member != None:
            embedfff.add_field(name='2 player', value=f'{member.global_name}')
            view = Shoulin(stx.author.id, member.id, embedfff)
            await stx.send(embed=embedfff,view=view)
        else:
            embedfff.add_field(name='2 player', value=None)
            view = Shoulin(stx.author.id, None, embedfff)
            await stx.send(embed=embedfff,view=view)

    @commands.slash_command()
    async def bull(self, interaction, member: disnake.Member):
        embedbull = disnake.Embed(colour='red' , title='Игра в быка', description=for_games.bull)
        embedbull.set_thumbnail(url="https://media.tproger.ru/uploads/2017/03/byk.png")
        embedbull.add_field(name='1 player', value=f'{interaction.author.global_name}')
        if member != None:
            embedbull.add_field(name='2 player', value=f'{member.global_name}')
            view = Shoulin(interaction.author.id, member.id, embedbull)
            await interaction.send(embed=embedbull,view=view)
        else:
            embedbull.add_field(name='2 player', value=None)
            view = Shoulin(interaction.author.id, None, embedbull)
            await interaction.send(embed=embedbull,view=view)        


#логирование сообщений, первая часть кода логирует в файл в более краткой форме, вторая часть логирует в файл и в #log
async def log(message: disnake.Message):
    now = datetime.datetime.now()
    # log_webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1242202771294261429/kch_F1G9r3k9SdQn1LzpOQtr4fSyuc9ZpAYfE_ad5GWPthLVXSCfIh8xhf_CUx8o-DIo')
    log_embed = Embed(
        title='Сообщение',
        description=message.content
    ).set_author(
        name=message.author.global_name,
        url=message.author.avatar.url
    )
    log_channel = await get_info(message.guild.id, 'logChannel')
    log_embed.add_field(name = 'Пользователь и его ID', value = f'{message.author.mention} ( {message.author.id} )', inline = False)
    log_embed.add_field(name = 'Дата', value = f'{now.strftime("%d/%m/%Y")}')
    log_embed.add_field(name = 'Время', value = f'{now.strftime("%H:%M:%S")}', inline=False)
    log_embed.add_field(name = 'Категория и её ID', value = f'{message.channel.category} ( {message.channel.category.id} )', inline=False)
    log_embed.add_field(name = 'Канал и его ID', value = f'{message.channel.mention} ( {message.channel.id} )')
    log_embed.add_field(name = 'Ссылка на сообщение', value = f'{message.jump_url}', inline=False)
    # log_webhook.add_embed(log_embed)
    channel = bot.get_channel(log_channel)
    await channel.send(embed=log_embed)
    # response = log_webhook.execute() 

@bot.event
async def on_message(message: disnake.Message):
    if message.webhook_id is not None:
        return
    await bot.process_commands(message)
    if message.author.bot != True:
        await log(message)
    await db_add_exp(message)


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

@bot.command()
async def test(ctx):
    await get_info(ctx.message.guild.id, 'logChannel')

@bot.command()
async def setLogChannel(stx):
    await set_log_channel(stx.message)   

class Shoulin(disnake.ui.View):
    def __init__(self, player1, player2 = None, embed = None):
        super().__init__(timeout=15.0)
        self.value: Optional[bool] = None
        self.player1: int = player1
        self.player2: int = player2
        self.player1_pick: str = None
        self.player2_pick: str = None
        self.embed: disnake.Embed = embed
        
    @disnake.ui.button(label='Камень', style=disnake.ButtonStyle.primary)
    async def vivod_texta(self,button:disnake.Button,interaction:disnake.Interaction):
        if self.player2 == None and interaction.author.id != self.player1:
            self.player2 = interaction.author.id
        if interaction.author.id == self.player1:
            self.player1_pick = 'rock'
        elif interaction.author.id == self.player2:
            self.player2_pick = 'rock'
        if self.player1_pick != None and self.player2_pick != None:
            embed = await self.winner()
            await interaction.response.edit_message(embed=embed, view=None)
    @disnake.ui.button(label='Ножницы', style=disnake.ButtonStyle.primary)
    async def vivod_texta2(self,button:disnake.Button,interaction:disnake.Interaction):
        if self.player2 == None and interaction.author.id != self.player1:
            self.player2 = interaction.author.id
        if interaction.author.id == self.player1:
            self.player1_pick = 'scissors'
        elif interaction.author.id == self.player2:
            self.player2_pick = 'scissors'
        if self.player1_pick != None and self.player2_pick != None:
            embed = await self.winner()
            await interaction.response.edit_message(embed=embed, view=None)
    
    @disnake.ui.button(label='Бумага', style=disnake.ButtonStyle.primary)
    async def vivod_texta3(self,button:disnake.Button,interaction:disnake.Interaction):
        if self.player2 == None and interaction.author.id != self.player1:
            self.player2 = interaction.author.id
        if interaction.author.id == self.player1:
            self.player1_pick = 'paper'
        elif interaction.author.id == self.player2:
            self.player2_pick = 'paper'
        if self.player1_pick != None and self.player2_pick != None:
            embed = await self.winner()
            await interaction.response.edit_message(embed=embed, view=None)

    async def winner(self):
        if self.player1_pick == self.player2_pick:
            embed = disnake.Embed(
                title='Ничья'
            )
            return embed
        elif self.player1_pick == 'paper' and self.player2_pick == 'rock':
            embed = disnake.Embed(
                title= 'Результы'
            )
            embed.add_field(name='Победитель', value= bot.get_user(self.player1).global_name)
            embed.add_field(name='Проигравший', value= bot.get_user(self.player2).global_name)
            embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Выбор', value= self.player1_pick)
            embed.add_field(name='Выбор', value= self.player2_pick)
            return embed
        elif self.player1_pick == 'rock' and self.player2_pick == 'scissors':
            embed = disnake.Embed(
                title= 'Результы'
            )
            embed.add_field(name='Победитель', value= bot.get_user(self.player1).global_name)
            embed.add_field(name='Проигравший', value= bot.get_user(self.player2).global_name)
            embed.add_field(name=' ', value= ' ', inline=False)
            embed.add_field(name='Выбор', value= self.player1_pick)
            embed.add_field(name='Выбор', value= self.player2_pick)
            return embed
        elif self.player1_pick == 'scissors' and self.player2_pick == 'paper':
            embed = disnake.Embed(
                title= 'Результы'
            )
            embed.add_field(name='Победитель', value= bot.get_user(self.player1).global_name)
            embed.add_field(name='Проигравший', value= bot.get_user(self.player2).global_name)
            embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Выбор', value= self.player1_pick)
            embed.add_field(name='Выбор', value= self.player2_pick)
            return embed
        else:
            embed = disnake.Embed(
                title= 'Результы'
            )
            embed.add_field(name='Победитель', value= bot.get_user(self.player2).global_name)
            embed.add_field(name='Проигравший', value= bot.get_user(self.player1).global_name)
            embed.add_field(name=' ', value= ' ', inline=False)
            embed.add_field(name='Выбор', value= self.player2_pick)
            embed.add_field(name='Выбор', value= self.player1_pick)
            return embed





bot.load_extensions("cogs")
bot.add_cog(ExpEvents(bot))
bot.add_cog(MiniGames(bot))

my_console.start()
bot.run(config.token)