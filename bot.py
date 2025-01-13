import discord
from config import *
from bot_commands import * 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Soy el bot de Jinbe jajaja")
    if message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    if message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    if message.content.startswith('$emojis'):
        await message.channel.send(gen_emojis())
    else:
        await message.channel.send(message.content)

client.run(settings["token"])

