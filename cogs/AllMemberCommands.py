import disnake
from asyncio import sleep
import disnake.ext.commands
import datetime
from disnake.ext import commands 
from disnake.utils import get

import disnake.ext 

class AllMemberCommands_slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
             description="Команды бота(как на русском, так и на английском языке"
    )
    async def info(self, interaction):

        embed = disnake.Embed(
        title="Заголовок эмбеда",
        description="Описание эмбеда",
        color=disnake.Colour.blue(),
        timestamp=datetime.datetime.now(),
        )

        embed.set_author(
        name="Project tw0 ( Bee ) by Beeeee and Mr.Krik",
        url="https://disnake.dev/",
        icon_url="https://disnake.dev/assets/disnake-logo.png",
        )
        embed.set_footer(
        text="Права не защищены, пошли нахуй, собственность интеллектуальная, а это мы, а рабство нахуй запрещено уебки.",
        icon_url="https://disnake.dev/assets/disnake-logo.png",
        )

        embed.set_thumbnail(url="https://disnake.dev/assets/disnake-logo.png")
        embed.set_image(url="https://disnake.dev/assets/disnake-thin-banner.png")

        embed.add_field(name="Обычный заголовок", value="Обычное значение", inline=False)
        embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)
        embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)
        embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)

        await interaction.send(embed=embed) 

        
                

# class AllMemberCommands(commands.Cog):                
#     def __init__(self, bot):
#         self.bot = bot
    
#     @commands.command()
#     async def delete(self, ctx, content):
#             if content.isdigit() == True:   
#                 content = int(content)
#                 await ctx.channel.purge(limit=content)
#                 await ctx.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(ctx.author.mention))
#                 await sleep(3)
#                 await ctx.channel.purge(limit=1)
#             elif content.isalpha():
#                 content = str(content.lower())
#                 if content == "all" or content == "все":
#                     await ctx.channel.purge(limit=100)
#                     await ctx.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(ctx.author.mention))
#                     await sleep(3)
#                     await ctx.channel.purge(limit=1)

#     @commands.command()
#     async def remove(self, ctx, rolename, member: disnake.Member = None):
#         if member is None:
#             member = ctx.author
#         role = get(ctx.guild.roles, name=rolename)
#         await member.remove_roles(role)
#         await ctx.send(f'Роль {rolename} убрана у {member.global_name}')

#     @commands.command()
#     async def give(self, ctx, rolename, member: disnake.Member = None):
#         if member is None:
#             member = ctx.author
#         role = get(ctx.guild.roles, name=rolename)
#         await member.add_roles(role)
#         await ctx.send(f'Роль {rolename} выдана {member.global_name}') 
    
#     @commands.command()    
#     async def timeout(self, ctx, member: disnake.Member, time: int, check: str, reason: str):
#         if check == "m" or check.lower() == "minutes":
#             time = datetime.datetime.now() + datetime.timedelta(minutes=time)

#         elif check == "s"  or check.lower() == "seconds":
#             time = datetime.datetime.now() + datetime.timedelta(seconds=time)

#         elif check == "h"  or check.lower() == "hours":
#             time = datetime.datetime.now() + datetime.timedelta(hours=time)

#         elif check == "d"  or check.lower() == "days":
#             time = datetime.datetime.now() + datetime.timedelta(days=time)

#         elif check == "w"  or check.lower() == "weeks":
#             time = datetime.datetime.now() + datetime.timedelta(weeks=time)
#         await member.timeout(until=time, reason=reason)
#         await ctx.send(f"Пользователь {member.mention} был затайм-аутен до {time.strftime('%H:%M:%S %d.%m.%Y')}")

#     @commands.command()
#     async def untimeout(self, ctx, member: disnake.Member):
#         await member.timeout(until=None, reason=None)
#         await ctx.send(f"Пользователь {member.mention} был разтайм-аутен")    

#     @commands.command()
#     async def ban(self, ctx, member: disnake.Member, reason: str):
#         await ctx.guild.ban(member, reason=reason)
#         await ctx.send(f"Пользователь {member.mention} был забанен по причине: {reason}")  

#     @commands.command()
#     async def forceban(ctx, member: disnake.User, reason: str):
#         await ctx.guild.ban(member, reason=reason)
#         await ctx.send(f"Пользователь {member.mention} был забанен по причине: {reason}")  

#     @commands.command()
#     async def unban(self, ctx, member: disnake.User):
#         await ctx.guild.unban(member) 
#         await ctx.send(f"Пользователь {member.mention} был разбанен.")

#     @commands.command()
#     async def get_member_id(self, ctx, member: disnake.User):
#         await ctx.author.send(member.id)
        
        
        



def setup(bot):
    bot.add_cog(AllMemberCommands_slash(bot))
    # bot.add_cog(AllMemberCommands(bot))             