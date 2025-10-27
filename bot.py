import random
import discord
from discord.ext import commands
import os 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


imgs = os.listdir('images')
print(os.listdir('images'))


@bot.command()
async def mem(ctx):
    imgs = os.listdir('images')
    img_name = random.choice(imgs)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


@bot.event
async def on_command_error(ctx, error):
    print(f"command error: {error}")
    await ctx.send(f"Error: {error}")
    

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    
    
@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return
    
    await before.channel.send("Wiadomość przed edycją: " + before.content)
    
    
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    
    
    
    
    
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    
    
    
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))



@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def trash(ctx):
    await ctx.send("niebieski: papier")
    await ctx.send("zielony: szkło")
    await ctx.send("żółty: metal i plastik")
    await ctx.send("czarny lub szary: zmieszane")
    await ctx.send("brazowy: bioodpady, np.resztki jedzenia")


@bot.command()
async def baterie(ctx):
    await ctx.send('Zamiast wyrzucić zużyte baterie, znajdź miejsce gdzie możesz je oddać. Baterie mają różne niebezpieczne substancje chemiczne, dlatego nie powinno się ich wyrzucac do zwykłych pojemników na śmieci.')

    
@bot.command()
async def helpme(ctx):
    await ctx.send("choose (podaj rzeczy do wybrania,bot wybierze jednom. np. kot pies chomik.)")
    await ctx.send("helpme (pokaże tą wiadomość)")
    await ctx.send("heh (wpisz heh i numer, bot wyświetli he tyle razy)")
    await ctx.send("hello (bot sie ztobom przywita)")
    await ctx.send("mem (wyświetli mega śmieszny mem)")
    await ctx.send("baterie (powie co sie robi z bateriami)")
    await ctx.send("trash (powie co sie wyrzuca do danego kosza)")




# to load, type in "python bot.py"


bot.run("")
