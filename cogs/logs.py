import disnake
import disnake.ext.commands
from disnake.ext import commands 
from disnake import Embed
import datetime

class Logs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author.bot != True:
            await self.log(message)

    #логирование сообщений в #log
    async def log(self, message: disnake.Message):
        now = datetime.datetime.now()
        log_embed = Embed(
            title='Сообщение',
            description=message.content
        ).set_author(
            name=message.author.global_name,
            url=message.author.avatar.url
        )
        info = self.bot.get_cog('DataBase')
        log_channel = await info.get_info(message.guild.id, 'logChannel')
        log_embed.add_field(name = 'Пользователь и его ID', value = f'{message.author.mention} ( {message.author.id} )', inline = False)
        log_embed.add_field(name = 'Дата', value = f'{now.strftime("%d/%m/%Y")}')
        log_embed.add_field(name = 'Время', value = f'{now.strftime("%H:%M:%S")}', inline=False)
        log_embed.add_field(name = 'Категория и её ID', value = f'{message.channel.category} ( {message.channel.category.id} )', inline=False)
        log_embed.add_field(name = 'Канал и его ID', value = f'{message.channel.mention} ( {message.channel.id} )')
        log_embed.add_field(name = 'Ссылка на сообщение', value = f'{message.jump_url}', inline=False)
        channel = self.bot.get_channel(log_channel)
        await channel.send(embed=log_embed) 

def setup(bot):
    bot.add_cog(Logs(bot))