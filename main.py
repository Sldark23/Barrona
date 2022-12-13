db["mesage"] = "oi"
from replit import db
import discord
import os
import requests
import json
import random
#from replit import db

persona = discord.Client()
parole_proibite = [
    "oi", "ola", "triste", "kkk", "gado", "olha o ban", "briga", "trolei", "?",
    "vc que sabe", "tudo bem", "comunista", "negro", "boa", "milagre", "fé",
    "minha loja no minecraft", "e doido", "vai dar namoro",
    "canta cheirou Red Bull", "meu mano a doido"
]
#asd=asd sono le rispote a parole proibite asd perchè non vorrei trovare problemi
#nel caso dovessi inserire automazioni del bot su certi ruoli nei server
asd = [
    "oi", "ola", "triste", "kkk", "gado", "olha o ban", "briga", "trolei", "?",
    "vc que sabe", "tudo bem", "comunista", "negro", "boa", "milagre", "fé",
    "minha loja no minecraft", "e doido", "vai dar namoro",
    "canta cheirou Red Bull", "meu mano e doido"
]

chiave_saluti = [
    "oi", "ola", "triste", "kkk", "gado", "olha o ban", "briga", "trolei", "?",
    "vc que sabe", "tudo bem", "comunista", "negro", "boa", "milagre", "fé",
    "minha loja no minecraft", "e doido", "vai dar namoro",
    "canta cheirou Red Bull", "meu mano e doido"
]

risposte_saluti = [
    "oi", "ola", "triste", "kkk", "gado", "olha o ban", "briga", "trolei", "?",
    "vc que sabe", "tudo bem", "comunista", "negro", "boa", "milagre", "fé",
    "minha loja no minecraft", "e doido", "vai dar namoro",
    "canta cheirou Red Bull", "meu mano e doido"
]

chiave_interazione = [
    "oi", "ola", "triste", "kkk", "gado", "olha o ban", "briga", "trolei", "?",
    "vc que sabe", "tudo bem", "comunista", "negro", "boa", "milagre", "fé",
    "minha loja no minecraft", "e doido", "vai dar namoro",
    "canta cheirou Red Bull", "meu mano e doido"
]

varie_dìvertenti = [
    "oi", "ola", "triste", "kkk", "gado", "olha o ban", "briga", "trolei", "?",
    "vc que sabe", "tudo bem", "comunista", "negro", "boa", "milagre", "fé",
    "minha loja no minecraft", "e doido", "vai dar namoro",
    "canta cheirou Red Bull", "meu mano e doido"
]


#Questa funziona mi serve per richiamare un processo del bot (frasi zen)
def get_quotes():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    #                    citazione                    autore
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return (quote)


"""def update_encouragement(enocuraging_message):
  if "encouragements" in db.keys():
   encouragements = db["encouragements"]
   encouragements.append(encouraging_message)
  else:
    db["encouragements"] = [encouraging_message]"""


@persona.event
async def on_ready():
    print("estou  {0.user}".format(persona))


@persona.event
async def on_message(message):
    if message.author == persona.user:
        return

    msg = message.content

    if msg.startswith("-zen"):
        quote = get_quotes()
        await message.channel.send(quote)

    if any(word in msg for word in parole_proibite):
        await message.channel.send(random.choice(asd))

    if any(word in msg for word in chiave_saluti):
        await message.channel.send(random.choice(risposte_saluti))

    if any(word in msg for word in chiave_interazione):
        await message.channel.send(random.choice(varie_dìvertenti))


persona.run(os.getenv("TOKEN"))
my_secret = os.environ['TOKEN']
