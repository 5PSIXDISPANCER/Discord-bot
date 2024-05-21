# Доработать
# @bot.command()
# async def play(ctx, yt):
#     if ctx.author.voice is None:
#         await ctx.send('Зайдите в войс канал и попробуйте снова')
#         return
#     yt = pytube.YouTube(yt)
#     stream = yt.streams.filter(only_audio=True).first().download()
#     await ctx.send(f"Видео успешно загружено! {yt}")
#     channel = ctx.message.author.voice.channel
#     await channel.connect()


# Функция удаления сообщений с аргументом в виде скольких сообщений будем дорабатоваться.
# import asyncio
# @bot.command()
# async def delete(ctx, content: int ):
#         await ctx.channel.purge(limit=content)
#         await ctx.send('Так нахуй, этот уебан удалил, ДА ДА ОН! {}'.format(ctx.author.mention))
#         await asyncio.sleep(5)
#         await ctx.channel.purge(limit=1)
# Хуйня о запуске, можно еще что-то добавить 
# @bot.event
# async def on_ready():
#     now = datetime.now()
#     guild = bot.get_guild(config.guild)
#     channel = bot.get_channel(1233069923492823162)
#     await channel.send(f"Работаю на хлопковой долине.\n Дата: {now.strftime("%d/%m/%Y")} \n Время: {now.strftime("%H:%M:%S")}")
#     user_1 = guild.get_member(config.soft_devolopment_dima) 
#     user_2 = guild.get_member(config.soft_devolopment_kirill)
#     await channel.send(f"Пидорасы, что меня разрабатывают и используют {user_1.mention} и {user_2.mention}")

111