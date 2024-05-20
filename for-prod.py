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
# внесение в конфиг soft_devolopment_dima = и тп
# Функция для записи в текствой файл даты и времени, автора с id и текстом сообщения + запись в канал





# Реализовано
# @bot.event
# async def on_message(ctx):
#     if ctx.author != bot.user:
#         f = open("Logs.txt", "a")
#         now = datetime.now()
#         f.write(f"Дата: {now.strftime("%d/%m/%Y")} Время: {now.strftime("%H:%M:%S")} Автор: {ctx.author} ({ctx.author.id}) Категория: {ctx.channel.category} ({ctx.channel.category.id}) Канал: {ctx.channel} ({ctx.channel.id}) Сообщение: {ctx.content}\n")
#         f.close()
#         channel = bot.get_channel(config.channel)
#         await channel.send(f"Дата: {now.strftime("%d/%m/%Y")} Время: {now.strftime("%H:%M:%S")} Автор: {ctx.author.mention} ({ctx.author.id}) Категория: {ctx.channel.category} ({ctx.channel.category.id}) Канал: {ctx.channel.mention} ({ctx.channel.id}) Сообщение: {ctx.jump_url}\n")