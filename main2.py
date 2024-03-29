import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Бот готов к работе!')

@bot.command()
async def разложение(ctx, предмет):
    if предмет == "бумага":
        await ctx.send("Бумажные изделия могут разлагаться от 2 до 6 недель в зависимости от условий.")
        await ctx.send("Для уменьшения количества мусора можно утилизировать бумагу через программы переработки или использовать для создания компоста.")
    elif предмет == "пластик":
        await ctx.send("Пластик может разлагаться от 450 лет до нескольких тысяч лет.")
        await ctx.send("Один из способов снижения загрязнения пластиком - повторное использование и переработка.")
    elif предмет == "стекло":
        await ctx.send("Стекло может разлагаться от 1 миллиона до нескольких миллионов лет.")
        await ctx.send("Стекло можно повторно использовать или перерабатывать в новые изделия.")
    elif предмет == "металл":
        await ctx.send("Некоторые металлические предметы могут разлагаться в течение сотен и тысяч лет, но могут также оставаться в почве неизменными на протяжении миллионов лет.")
        await ctx.send("Металлы можно перерабатывать для создания новых изделий, что снижает необходимость в добыче новых ресурсов.")
    elif предмет == "органика":
        await ctx.send("Органические материалы могут разлагаться от нескольких недель до нескольких лет в зависимости от условий.")
        await ctx.send("Органические отходы можно компостировать, что способствует уменьшению объема мусора и созданию питательного грунта.")
    else:
        await ctx.send("Извините, я не знаю, сколько времени требуется для разложения этого предмета.")

@bot.command()
async def статистика(ctx):
    # Здесь может быть запрос к внешнему API или базе данных для получения статистики использования материалов
    await ctx.send("Статистика использования материалов пока недоступна.")

@bot.command()
async def совет(ctx, предмет):
    if предмет == "пластик":
        await ctx.send("Попробуйте избегать одноразового использования пластиковых изделий и переходите на перерабатываемые альтернативы.")
    elif предмет == "бумага":
        await ctx.send("Используйте обе стороны бумаги и рассматривайте возможность перехода на цифровые документы для снижения потребления бумаги.")
    elif предмет == "органика":
        await ctx.send("Создавайте компост из органических отходов, чтобы уменьшить объем отходов и получить питательный грунт для сада или огорода.")
    else:
        await ctx.send("Извините, советы по этому материалу пока недоступны.")

@bot.command()
async def викторина(ctx):
    вопросы = [
        ("Какой материал разлагается дольше всего? (а) Пластик (б) Стекло (в) Органика", "а"),
        ("Что можно сделать из бумаги, чтобы уменьшить количество мусора? (а) Сжечь (б) Утилизировать (в) Переработать", "в"),
        ("Какой вид материала можно использовать для создания компоста? (а) Пластик (б) Стекло (в) Органика", "в")
    ]
    вопрос, ответ = random.choice(вопросы)
    await ctx.send(вопрос)

    def проверка_ответа(message):
        return message.author == ctx.author and message.content.lower() in ['а', 'б', 'в']

    сообщение = await bot.wait_for('message', check=проверка_ответа)
    if сообщение.content.lower() == ответ:
        await ctx.send("Правильно!")
    else:
        await ctx.send(f"Неправильно. Правильный ответ: {ответ}")

@bot.command()
async def обзор(ctx):
    # Здесь может быть запрос к внешнему API или базе данных для получения обзора научных исследований
    await ctx.send("Обзор научных исследований пока недоступен.")

bot.run('твой_токен')
