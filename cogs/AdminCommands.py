import disnake
from asyncio import sleep
import disnake.ext.commands
import datetime
from disnake.ext import commands 
from disnake.utils import get

import disnake.ext 

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
             description="Удаление сообщений. Либо кол-во сообщений  или слово все (русский или английский язык)"
    )
    async def delete(self, interaction, content):
            if content.isdigit() == True:   
                content = int(content)
                await interaction.channel.purge(limit=content)
                await interaction.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(interaction.author.mention), ephemeral=False)
                await sleep(3)
                await interaction.channel.purge(limit=1)
            elif content.isalpha():
                content = str(content.lower())
                if content == "all" or content == "все":
                    await interaction.channel.purge(limit=100)
                    await interaction.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(interaction.author.mention), ephemeral=False)
                    await sleep(3)
                    await interaction.channel.purge(limit=1)

    @commands.slash_command(
            description="Снятие роли"
    )
    async def remove(self, interaction, member: disnake.Member, role: str ):
        role = get(interaction.guild.roles, name=role)
        await member.remove_roles(role)
        await interaction.response.send_message(f'Роль {role} убрана у {member.mention}', ephemeral=False)

    @commands.slash_command(
            description="Добавление роли"
    )
    async def give(self, interaction, member: disnake.Member, role: str):
        role = get(interaction.guild.roles, name=role)
        await member.add_roles(role)
        await interaction.response.send_message(f'Роль {role} выдана {member.mention}', ephemeral=False)

    @commands.slash_command(
            description="Выдача таймаута. Переменная чек принимает меру исчисления s-seconds и т.д"
    )
    async def timeout(self, interaction, member: disnake.Member, time: int, check: str, reason: str):
        if check == "m" or check.lower() == "minutes":
            time = datetime.datetime.now() + datetime.timedelta(minutes=time)

        elif check == "s"  or check.lower() == "seconds":
            time = datetime.datetime.now() + datetime.timedelta(seconds=time)

        elif check == "h"  or check.lower() == "hours":
            time = datetime.datetime.now() + datetime.timedelta(hours=time)

        elif check == "d"  or check.lower() == "days":
            time = datetime.datetime.now() + datetime.timedelta(days=time)

        elif check == "w"  or check.lower() == "weeks":
            time = datetime.datetime.now() + datetime.timedelta(weeks=time)
        await member.timeout(until=time, reason=reason)
        await interaction.response.send_message(f"Пользователь {member.mention} был затайм-аутен до {time.strftime('%H:%M:%S %d.%m.%Y')}",ephemeral=False)

    @commands.slash_command()  
    async def ban(self, interaction, member: disnake.Member, reason: str):
        await interaction.guild.ban(member, reason=reason)
        await interaction.response.send_message(f"Пользователь {member.mention} был забанен по причине: {reason}", ephemeral=False)  

    @commands.slash_command()  
    async def unban(self, interaction, member: disnake.User):
        await interaction.guild.unban(member) 
        await interaction.response.send_message(f"Пользователь {member.mention} был разбанен.", ephemeral=False)

    @commands.slash_command()
    async def untimeout(self, interaction, member: disnake.Member):
        await member.timeout(until=None, reason=None)
        await interaction.response.send_message(f"Пользователь {member.mention} был разтайм-аутен", ephemeral=False)



def setup(bot):
    bot.add_cog(AdminCommands(bot))        