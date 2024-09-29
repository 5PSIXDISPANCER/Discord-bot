import disnake
from asyncio import sleep
import disnake.ext.commands
import datetime
from disnake.ext import commands 
from disnake.utils import get

import disnake.ext 

adminPermission = disnake.Permissions(administrator=True, kick_members=True, ban_members=True, mute_members=True)

class AdminCommands_slash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
             description="Удаление сообщений. Либо кол-во сообщений  или слово все (русский или английский язык)",
             default_member_permissions= adminPermission
    )
    async def delete(self, interaction, content, hide: bool = True):
            if content.isdigit() == True:   
                content = int(content)
                await interaction.channel.purge(limit=content)
                await interaction.send(f'Так нахуй, этот уебан удалил: {interaction.author.mention} - ДА ДА ОН!', ephemeral=hide)
                if hide == True:
                    return
                await sleep(3)
                await interaction.channel.purge(limit=1)
            elif content.isalpha():
                content = str(content.lower())
                if content == "all" or content == "все":
                    await interaction.channel.purge(limit=100)
                    await interaction.send(f'Так нахуй, этот уебан удалил: {interaction.author.mention} - ДА ДА ОН!', ephemeral=hide)
                    if hide == True:
                      return
                    await sleep(3)
                    await interaction.channel.purge(limit=1)

    @commands.slash_command(
            description="Снятие роли",
    )
    async def remove(self, interaction, member: disnake.Member, role: str, hide: bool):
        role = get(interaction.guild.roles, name=role)
        await member.remove_roles(role)
        await interaction.response.send_message(f'Роль {role} убрана у {member.mention}', ephemeral=hide)

    @commands.slash_command(
            description="Добавление роли",
            default_member_permissions= adminPermission
    )
    async def give(self, interaction, member: disnake.Member, role: str, hide: bool):
        role = get(interaction.guild.roles, name=role)
        await member.add_roles(role)
        await interaction.response.send_message(f'Роль {role} выдана {member.mention}', ephemeral=hide)

    @commands.slash_command(
            description="Выдача таймаута, переменная чек принимает меру исчисления (s)econds и т.д.",
            default_member_permissions= adminPermission
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
            description="Снятие таймаута",
            default_member_permissions= adminPermission
    )
    async def untimeout(self, interaction, member: disnake.Member, hide: bool):
        await member.timeout(until=None, reason=None)
        await interaction.response.send_message(f"Пользователь {member.mention} был разтайм-аутен", ephemeral=hide)    

    @commands.slash_command(
            description="Бан с причиной",
            default_member_permissions= adminPermission
    )  
    async def ban(self, interaction, member: disnake.Member, reason: str, hide: bool):
        await interaction.guild.ban(member, reason=reason)
        await interaction.response.send_message(f"Пользователь {member.mention} был забанен по причине: {reason}", ephemeral=hide)  

    @commands.slash_command(
        description="Бан пользователя дискорда, если его нет на сервере",
        default_member_permissions= adminPermission
    )       
    async def forceban(self, interaction, member: disnake.User, hide: bool):
        await interaction.guild.unban(member) 
        await interaction.response.send_message(f"Пользователь {member.mention} был забанен", ephemeral=hide)

    @commands.slash_command(
        description="Снятие бана",
        default_member_permissions= adminPermission
    )  
    async def unban(self, interaction, member: disnake.User, hide: bool):
        await interaction.guild.unban(member) 
        await interaction.response.send_message(f"Пользователь {member.mention} был разбанен", ephemeral=hide)

    @commands.slash_command(
        description="Возвращение id участника",
        default_member_permissions= adminPermission
    )  
    async def get_member_id(self, interaction, member: disnake.User, hide: bool):
        await interaction.response.send_message(f"ID пользователя  {member.id}", ephemeral=hide)


class AdminCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
    async def delete(self, ctx, content):
            if content.isdigit() == True:   
                content = int(content)
                await ctx.channel.purge(limit=content)
                await ctx.send(f'Так нахуй, этот уебан удалил: {ctx.author.mention} - ДА ДА ОН! ')
                await sleep(3)
                await ctx.channel.purge(limit=1)
            elif content.isalpha():
                content = str(content.lower())
                if content == "all" or content == "все":
                    await ctx.channel.purge(limit=100)
                    await ctx.send(f'Так нахуй, этот уебан удалил: {ctx.author.mention} - ДА ДА ОН! ')
                    await sleep(3)
                    await ctx.channel.purge(limit=1)

    @commands.command()
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
    async def remove(self, ctx, rolename, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        role = get(ctx.guild.roles, name=rolename)
        await member.remove_roles(role)
        await ctx.send(f'Роль {rolename} убрана у {member.global_name}')

    @commands.command()
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
    async def give(self, ctx, rolename, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        role = get(ctx.guild.roles, name=rolename)
        await member.add_roles(role)
        await ctx.send(f'Роль {rolename} выдана {member.global_name}') 
    
    @commands.command()    
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
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
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
    async def untimeout(self, ctx, member: disnake.Member):
        await member.timeout(until=None, reason=None)
        await ctx.send(f"Пользователь {member.mention} был разтайм-аутен")    

    @commands.command()
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
    async def ban(self, ctx, member: disnake.Member, reason: str):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"Пользователь {member.mention} был забанен по причине: {reason}")  

    @commands.command()
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
    async def forceban(ctx, member: disnake.User, reason: str):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"Пользователь {member.mention} был забанен по причине: {reason}")  

    @commands.command()
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
    async def unban(self, ctx, member: disnake.User):
        await ctx.guild.unban(member) 
        await ctx.send(f"Пользователь {member.mention} был разбанен.")

    @commands.command()
    @commands.has_permissions(administrator=True, kick_members=True, ban_members=True)
    async def get_member_id(self, ctx, member: disnake.User):
        await ctx.author.send(member.id)
        
        
        



def setup(bot):
    bot.add_cog(AdminCommands_slash(bot))
    bot.add_cog(AdminCommands(bot))             