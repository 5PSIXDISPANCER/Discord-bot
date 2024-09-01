import disnake
import disnake.ext.commands
import config
from dpyConsole import Console
from disnake.ext import commands 
import disnake.ext 

intents = disnake.Intents().all() #разрешения
bot = commands.Bot(command_prefix=config.prefix, intents=intents, test_guilds=[1232407034108973186]) #префикс команд и разрешения
my_console = Console(bot)

@bot.event
async def on_message(message: disnake.Message):
    if message.webhook_id is not None:
        return
    await bot.process_commands(message)

bot.load_extensions("cogs")

my_console.start()
bot.run(config.token)