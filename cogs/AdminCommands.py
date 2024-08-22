import disnake
from asyncio import sleep
import disnake.ext.commands
import datetime
from disnake.ext import commands 
from disnake.utils import get
import db

import disnake.ext 

class AdminCommands_slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
             description="Удаление сообщений. Либо кол-во сообщений  или слово все (русский или английский язык)"
    )
    async def delete(self, interaction, content, hide: bool):
            if content.isdigit() == True:   
                content = int(content)
                await interaction.channel.purge(limit=content)
                await interaction.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(interaction.author.mention), ephemeral=hide)
                await sleep(3)
                await interaction.channel.purge(limit=1)
            elif content.isalpha():
                content = str(content.lower())
                if content == "all" or content == "все":
                    await interaction.channel.purge(limit=100)
                    await interaction.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(interaction.author.mention), ephemeral=hide)
                    await sleep(3)
                    await interaction.channel.purge(limit=1)

    @commands.slash_command(
            description="Снятие роли"
    )
    async def remove(self, interaction, member: disnake.Member, role: str, hide: bool):
        role = get(interaction.guild.roles, name=role)
        await member.remove_roles(role)
        await interaction.response.send_message(f'Роль {role} убрана у {member.mention}', ephemeral=hide)

    @commands.slash_command(
            description="Добавление роли"
    )
    async def give(self, interaction, member: disnake.Member, role: str, hide: bool):
        role = get(interaction.guild.roles, name=role)
        await member.add_roles(role)
        await interaction.response.send_message(f'Роль {role} выдана {member.mention}', ephemeral=hide)

    @commands.slash_command(
            description="Выдача таймаута, переменная чек принимает меру исчисления (s)econds и т.д."
    )
    async def timeout(self, interaction, member: disnake.Member, time: int, check: str, reason: str, hide: bool):
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
        await interaction.response.send_message(f"Пользователь {member.mention} был затайм-аутен до {time.strftime('%H:%M:%S %d.%m.%Y')}",ephemeral=hide)

    @commands.slash_command(
            description="Снятие таймаута"
    )
    async def untimeout(self, interaction, member: disnake.Member, hide: bool):
        await member.timeout(until=None, reason=None)
        await interaction.response.send_message(f"Пользователь {member.mention} был разтайм-аутен", ephemeral=hide)    

    @commands.slash_command(
            description="Бан с причиной"
    )  
    async def ban(self, interaction, member: disnake.Member, reason: str, hide: bool):
        await interaction.guild.ban(member, reason=reason)
        await interaction.response.send_message(f"Пользователь {member.mention} был забанен по причине: {reason}", ephemeral=hide)  

    @commands.slash_command(
        description="Бан пользователя дискорда, если его нет на сервере"
    )       
    async def forceban(self, interaction, member: disnake.User, hide: bool):
        await interaction.guild.unban(member) 
        await interaction.response.send_message(f"Пользователь {member.mention} был забанен", ephemeral=hide)

    @commands.slash_command(
            description="Снятие бана"
    )  
    async def unban(self, interaction, member: disnake.User, hide: bool):
        await interaction.guild.unban(member) 
        await interaction.response.send_message(f"Пользователь {member.mention} был разбанен", ephemeral=hide)

    @commands.slash_command(
        description="Возвращение id участника"
    )  
    async def get_member_id(self, interaction, member: disnake.User, hide: bool):
        await interaction.response.send_message(f"ID пользователя  {member.id}", ephemeral=hide)


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def delete(self, ctx, content):
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

    @commands.command()
    async def remove(self, ctx, rolename, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        role = get(ctx.guild.roles, name=rolename)
        await member.remove_roles(role)
        await ctx.send(f'Роль {rolename} убрана у {member.global_name}')

    @commands.command()
    async def give(self, ctx, rolename, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        role = get(ctx.guild.roles, name=rolename)
        await member.add_roles(role)
        await ctx.send(f'Роль {rolename} выдана {member.global_name}') 
    
    @commands.command()    
    async def timeout(self, ctx, member: disnake.Member, time: int, check: str, reason: str):
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
        await ctx.send(f"Пользователь {member.mention} был затайм-аутен до {time.strftime('%H:%M:%S %d.%m.%Y')}")

    @commands.command()
    async def untimeout(self, ctx, member: disnake.Member):
        await member.timeout(until=None, reason=None)
        await ctx.send(f"Пользователь {member.mention} был разтайм-аутен")    

    @commands.command()
    async def ban(self, ctx, member: disnake.Member, reason: str):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"Пользователь {member.mention} был забанен по причине: {reason}")  

    @commands.command()
    async def forceban(ctx, member: disnake.User, reason: str):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"Пользователь {member.mention} был забанен по причине: {reason}")  

    @commands.command()
    async def unban(self, ctx, member: disnake.User):
        await ctx.guild.unban(member) 
        await ctx.send(f"Пользователь {member.mention} был разбанен.")

    @commands.command()
    async def get_member_id(self, ctx, member: disnake.User):
        await ctx.author.send(member.id)
        
        
        



def setup(bot):
    bot.add_cog(AdminCommands_slash(bot))
    bot.add_cog(AdminCommands(bot))             