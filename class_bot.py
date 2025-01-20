import discord
import random
from discord.ext import commands
from config import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logeamos como {bot.user} correctamente ✅.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!, el de jinbe jajajaj')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# Comando de ayuda.
@bot.command()
async def helpop(ctx):
    help = discord.Embed(
        title="Comandos del bot 🤖",
        description="Estos son algunos comandos del bot Jinbe 😁",
        color=discord.Color.green()
    )
    help.set_thumbnail(url='https://i.imgur.com/V56GoSv.jpeg')
    help.set_author(name='Jinbe Bot', icon_url='https://i.imgur.com/V56GoSv.jpeg') 
    help.set_image(url='https://i.imgur.com/V56GoSv.jpeg')
    help.set_footer(text="Jinbe Bot", icon_url='https://i.imgur.com/V56GoSv.jpeg')

    # Añadir campos al embed
    help.add_field(name="$hello", value="Saluda al bot", inline=False)
    help.add_field(name="$heh", value="Multiplica una palabra x5", inline=False)
    help.add_field(name="$add", value="Agrega dos numeros para ser sumados.", inline=False)

    await ctx.send(embed=help)

bot.run(settings['token'])