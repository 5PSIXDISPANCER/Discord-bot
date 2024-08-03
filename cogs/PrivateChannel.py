import disnake
from asyncio import sleep
import disnake.ext.commands
import datetime
from disnake.ext import commands 
from disnake.utils import get
from disnake import TextInputStyle
import disnake.ext 
channel_creater = 1232752259407020193






class MyModal(disnake.ui.Modal):
    def __init__(self):

        components = [
            disnake.ui.TextInput(
                label="Название канала",
                placeholder="Не более 45 символов",
                custom_id="name",
                style=TextInputStyle.single_line,
                max_length=45,
                min_length=1
            ),
            disnake.ui.TextInput(
                label="NSFW",
                placeholder="Да или нет",
                custom_id="NSFW",
                style=TextInputStyle.short,
                max_length=3,
                min_length=2
            ),
            
            disnake.ui.TextInput(
                label="Приватный?",
                placeholder="Да или нет",
                custom_id="private",
                style=TextInputStyle.short,
                max_length=3,
                min_length=2
            ), 

            disnake.ui.TextInput(
                label="Лимит пользователей",
                placeholder="0 или нет, в противном число до 99",
                custom_id="limit_people",
                style=TextInputStyle.short,
                max_length=2,
                min_length=0
            )
        ]



        super().__init__(title="Создание канала", components=components)

    # async def callback(self, inter: disnake.ModalInteraction):
       

        

class PrivateChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: disnake.Member, before: disnake.VoiceState, after: disnake.VoiceState ):
        if after.channel.id == channel_creater:
            pass


        else:
            pass    

class Modal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def tags(inter: disnake.AppCmdInter):
        await inter.response.send_modal(modal=MyModal())    


def setup(bot):
    bot.add_cog(PrivateChannel(bot))
    bot.add_cog(Modal(bot))
