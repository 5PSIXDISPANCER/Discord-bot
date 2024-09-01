import disnake
import disnake.ext.commands
import config
import datetime
from dpyConsole import Console
from disnake import Embed 
from disnake.ext import commands 
import disnake.ext 


#Переменные необходимые в коде, для его сокращения.
intents = disnake.Intents().all() #разрешения
bot = commands.Bot(command_prefix=config.prefix, intents=intents, test_guilds=[1232407034108973186]) #префикс команд и разрешения
my_console = Console(bot)


#логирование сообщений, первая часть кода логирует в файл в более краткой форме, вторая часть логирует в файл и в #log
async def log(message: disnake.Message):
    now = datetime.datetime.now()
    log_embed = Embed(
        title='Сообщение',
        description=message.content
    ).set_author(
        name=message.author.global_name,
        url=message.author.avatar.url
    )
    info = bot.get_cog('DataBase')
    log_channel = await info.get_info(message.guild.id, 'logChannel')
    log_embed.add_field(name = 'Пользователь и его ID', value = f'{message.author.mention} ( {message.author.id} )', inline = False)
    log_embed.add_field(name = 'Дата', value = f'{now.strftime("%d/%m/%Y")}')
    log_embed.add_field(name = 'Время', value = f'{now.strftime("%H:%M:%S")}', inline=False)
    log_embed.add_field(name = 'Категория и её ID', value = f'{message.channel.category} ( {message.channel.category.id} )', inline=False)
    log_embed.add_field(name = 'Канал и его ID', value = f'{message.channel.mention} ( {message.channel.id} )')
    log_embed.add_field(name = 'Ссылка на сообщение', value = f'{message.jump_url}', inline=False)
    channel = bot.get_channel(log_channel)
    await channel.send(embed=log_embed) 

@bot.event
async def on_message(message: disnake.Message):
    if message.webhook_id is not None:
        return
    await bot.process_commands(message)
    if message.author.bot != True:
        await log(message)


bot.load_extensions("cogs")

my_console.start()
bot.run(config.token)