import disnake
import disnake.ext.commands
from disnake.ext import commands 
from typing import Optional


class MiniGames(commands.Cog):
    def __init__(self, bot: commands.Bot):
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
            view = Shoulin(stx.author.id, member.id, embedfff, self.bot)
            await stx.send(embed=embedfff,view=view)
        else:
            embedfff.add_field(name='2 player', value=None)
            view = Shoulin(stx.author.id, None, embedfff, self.bot)
            await stx.send(embed=embedfff,view=view)

    # Что это?
    # @commands.slash_command()
    # async def bull(self, interaction, member: disnake.Member):
    #     embedbull = disnake.Embed(colour='red' , title='Игра в быка', description=for_games.bull)
    #     embedbull.set_thumbnail(url="https://media.tproger.ru/uploads/2017/03/byk.png")
    #     embedbull.add_field(name='1 player', value=f'{interaction.author.global_name}')
    #     if member != None:
    #         embedbull.add_field(name='2 player', value=f'{member.global_name}')
    #         view = Shoulin(interaction.author.id, member.id, embedbull)
    #         await interaction.send(embed=embedbull,view=view)
    #     else:
    #         embedbull.add_field(name='2 player', value=None)
    #         view = Shoulin(interaction.author.id, None, embedbull)
    #         await interaction.send(embed=embedbull,view=view)


# Support class for mini games

# Добавить пояснение к параметрам
class Shoulin(disnake.ui.View):
    def __init__(self, player1, player2 = None, embed = None, bot = None):
        super().__init__(timeout=15.0)
        # Что делает строка ниже?
        self.value: Optional[bool] = None
        self.bot = bot
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
            embed.add_field(name='Победитель', value= self.bot.get_user(self.player1).global_name)
            embed.add_field(name='Проигравший', value= self.bot.get_user(self.player2).global_name)
            embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Выбор', value= self.player1_pick)
            embed.add_field(name='Выбор', value= self.player2_pick)
            return embed
        elif self.player1_pick == 'rock' and self.player2_pick == 'scissors':
            embed = disnake.Embed(
                title= 'Результы'
            )
            embed.add_field(name='Победитель', value= self.bot.get_user(self.player1).global_name)
            embed.add_field(name='Проигравший', value= self.bot.get_user(self.player2).global_name)
            embed.add_field(name=' ', value= ' ', inline=False)
            embed.add_field(name='Выбор', value= self.player1_pick)
            embed.add_field(name='Выбор', value= self.player2_pick)
            return embed
        elif self.player1_pick == 'scissors' and self.player2_pick == 'paper':
            embed = disnake.Embed(
                title= 'Результы'
            )
            embed.add_field(name='Победитель', value= self.bot.get_user(self.player1).global_name)
            embed.add_field(name='Проигравший', value= self.bot.get_user(self.player2).global_name)
            embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Выбор', value= self.player1_pick)
            embed.add_field(name='Выбор', value= self.player2_pick)
            return embed
        else:
            embed = disnake.Embed(
                title= 'Результы'
            )
            embed.add_field(name='Победитель', value= self.bot.get_user(self.player2).global_name)
            embed.add_field(name='Проигравший', value= self.bot.get_user(self.player1).global_name)
            embed.add_field(name=' ', value= ' ', inline=False)
            embed.add_field(name='Выбор', value= self.player2_pick)
            embed.add_field(name='Выбор', value= self.player1_pick)
            return embed
        
def setup(bot):
    bot.add_cog(MiniGames(bot))