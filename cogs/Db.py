import pymongo
import disnake
import disnake.ext.commands
from disnake.ext import commands 



class DataBase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = pymongo.MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6')
        self.db = self.client['beebot']
        self.coll = self.db['serverList']

    @commands.command()    
    async def create_db(self, ctx):
        db = self.db
        coll = self.coll
        coll.insert_one({'field':'value'})
        coll.delete_one({'field':'value'})

    @commands.command()
    async def dblogging(self, ctx):
        coll = self.db.serverList
        if 'serverList'not in self.db.list_collection_names():
            print('coll is missing')
        else:
            coll.delete_many({})
            requestArray = []
            for i in range(len(self.bot.guilds)):
                request = {}
                request['_id'] = self.bot.guilds[i].id
                request['servername'] = self.bot.guilds[i].name
                membersName = {}
                for x in range(len(self.bot.guilds[i].members)):
                    membersName[self.bot.guilds[i].members[x].name.replace('.', '')] = 0
                request['membersName'] = membersName
                requestArray.append(request)
            coll.insert_many(requestArray)
        print("База перезапущена")

    @commands.command()
    async def db_add_guild(self, guild: disnake.Guild):
        if 'serverList'not in self.db.list_collection_names():
            print('coll is missing')
        else:
            request = {}
            request['_id'] = guild.id
            request['servername'] = guild.name
            membersName = {}
            for x in range(len(guild.members)):
                membersName[guild.members[x].name.replace('.', '')] = 0
            request['membersName'] = membersName
            self.coll.insert_one(request)

    @commands.command()
    # replace dslkfjsdfljf fix pls
    async def db_add_exp(self, message: disnake.Message):
        if message.content[0] == '!':
            return
        exp = int(len(message.content.replace(' ', '')))
        print(exp)
        print(message.author.name)
        self.coll.update_one({'_id': message.guild.id}, {'$inc': {f'membersName.{message.author.name.replace('.', '')}': +exp}})
    
    @commands.command(name='dsfsdfsdfsegh')
    async def db_get_exp(self, ctx: disnake.Message):
        for value in self.coll.find({'_id': ctx.guild.id}, {'_id': 0,'membersName': 1}):
            return value['membersName'][ctx.author.name.replace('.', '')]
    
    @commands.command()
    async def set_log_channel(self,message: disnake.Message):
        self.coll.update_one({'_id': message.guild.id},{'$set': {'logChannel': int(message.content.split(' ')[1])}})
    
    @commands.command()
    async def get_info(self, guildId, znach: str):
        return self.coll.find_one({'_id' :guildId},{znach: 1})[znach]
    
def setup(bot):
    bot.add_cog(DataBase(bot))      