import disnake
import datetime
from disnake.ext import commands
import disnake.ext.commands
import disnake.ext


class ExpEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild: disnake.Guild):
        db = self.bot.get_cog('DataBase')
        print('Join working')
        await db.db_add_guild(guild)

    @commands.command()
    async def exp(self, stx: disnake.ext.commands.context.Context):
        db = self.bot.get_cog('DataBase')
        response = await db.db_get_exp(stx)
        embed = disnake.Embed(
            description = f"Количество опыта: {response}",
            color = disnake.Colour.yellow(),
            timestamp = datetime.datetime.now()
        )
        embed.set_author(
            name = stx.author.global_name,
            icon_url = stx.author.avatar.url
        )
        await stx.send(embed=embed)
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello ... This feels familiar.')


def setup(bot):
    bot.add_cog(ExpEvents(bot))      
