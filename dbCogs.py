from typing import Any
import pymongo
import discord
from discord.ext import commands 
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')
db = client['beebot']
coll = db['serverList']


class DataBase(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()    
    async def create_db():
        db = client['beebot']
        coll = db['serverList']
        coll.insert_one({'field':'value'})
        coll.delete_one({'field':'value'})

    @commands.command()
    async def dblogging(bot: commands.Bot):
        coll = db.serverList
        if 'serverList'not in db.list_collection_names():
            print('coll is missing')
        else:
            coll.delete_many({})
            requestArray = []
            for i in range(len(bot.guilds)):
                request = {}
                request['_id'] = bot.guilds[i].id
                request['servername'] = bot.guilds[i].name
                membersName = {}
                for x in range(len(bot.guilds[i].members)):
                    membersName[bot.guilds[i].members[x].name.replace('.', '')] = 0
                request['membersName'] = membersName
                requestArray.append(request)
            coll.insert_many(requestArray)
        print("База перезапущена")

    @commands.command()
    async def db_add_guild(guild):
        if 'serverList'not in db.list_collection_names():
            print('coll is missing')
        else:
            request = {}
            request['_id'] = guild.id
            request['servername'] = guild.name
            membersName = {}
            for x in range(len(guild.members)):
                membersName[guild.members[x].name.replace('.', '')] = 0
            request['membersName'] = membersName
            coll.insert_one(request)

    @commands.command()
    # replace dslkfjsdfljf fix pls
    async def db_add_exp(message: discord.Message):
        if message.content[0] == '!':
            return
        exp = int(len(message.content.replace(' ', '')))
        print(exp)
        print(message.author.name)
        coll.update_one({'_id': message.guild.id}, {'$inc': {f'membersName.{message.author.name.replace('.', '')}': +exp}})
    
    @commands.command()
    async def db_get_exp(ctx):
        for value in coll.find({'_id': ctx.guild.id}, {'_id': 0,'membersName': 1}):
            return value['membersName'][ctx.author.name.replace('.', '')]
    
    @commands.command()
    async def set_log_channel(message: discord.Message):
        coll.update_one({'_id': message.guild.id},{'$set': {'logChannel': int(message.content.split(' ')[1])}})
    
    @commands.command()
    async def get_info(guildId, znach):
        return coll.find_one({'_id' :guildId},{znach: 1})[znach]