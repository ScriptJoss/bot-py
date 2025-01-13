# Comandos del bot, nada importante

import random

# Generador de contraseñas
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

# Generador de emojis
def gen_emojis():
    emojis = [
    "\U0001F60A",  # 😊
    "\U0001F609",  # 😉
    "\U0001F623",  # 😣
    "\U0001F637",  # 😷
    "\U0001F929",  # 🤩
    "\U0001F914",  # 🤔
    "\U0001F61F",  # 😟
    "\U0001F620",  # 😠
    "\U0001F625",  # 😥
    "\U0001F634",  # 😴
]
    return random.choice(emojis)