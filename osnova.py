import disnake
from random import shuffle
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

@bot.command()
async def roulete(ctx: disnake.ext.commands.Context ,gameMembers: int):
    memberCount = 0
    startEmbed = disnake.Embed(title='Автор рулетки')
    startEmbed.set_author(name='Roulete')
    startEmbed.add_field(name=ctx.author.global_name ,value='', inline=False)
    startEmbed.add_field(name=f'Люди ({memberCount}/{gameMembers})', value='', inline=False)
    view = Roulete_Start_Menu(startEmbed=startEmbed, gameAuthorID = ctx.author.id, gameMebers=gameMembers)
    await ctx.send(embed=startEmbed, view=view)

class Roulete_Start_Menu(disnake.ui.View):
    def __init__(self, startEmbed: disnake.Embed, gameAuthorID: int, gameMebers: int):
        super().__init__(timeout=None)
        self.startEmbed = startEmbed
        self.gameAuthorID = gameAuthorID
        self.gameMebers = gameMebers
        self.memberCount = []
        self.round: int = 1
        self.gameStart: bool = False
    
    @disnake.ui.button(label="Начать игру", style=disnake.ButtonStyle.primary)
    async def Start(self, button:disnake.ui.Button, interaction:disnake.Interaction):
        await self.startGame(interaction=interaction)
    
    @disnake.ui.button(label="Вступить в игру", style=disnake.ButtonStyle.primary)
    async def Join(self,button:disnake.Button,interaction:disnake.Interaction):
        self.memberCount.append(interaction.author.global_name)
        self.startEmbed.set_field_at(index=1, name=f'Люди {len(self.memberCount)}/{self.gameMebers}',value=', '.join(self.memberCount) , inline=False)
        if len(self.memberCount) == self.gameMebers:
            button.disabled = True
        await interaction.response.edit_message(embed=self.startEmbed, view=self)

    async def startGame(self, interaction:disnake.Interaction):
        baraban = [0,0,0,0,0,1]
        shuffle(baraban)
        print(self.children[0])
        print(baraban)
        self.Start.disabled = True
        gameEmbed = disnake.Embed(title=f'Раунд {self.round}')
        gameEmbed.add_field(value='\n'.join(self.memberCount), name='Очередь', inline=False)
        await interaction.response.edit_message(embed=gameEmbed, components=self.children[0])

class Roulete_Game(disnake.ui.View):
    def __init__(self):
        super().__init__()

bot.load_extensions("cogs")

my_console.start()
bot.run(config.token)