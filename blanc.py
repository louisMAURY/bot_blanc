from discord import *

token = "NTYyMzU0NjAwNDk4NDI5OTc5.XKJlXw.32K4BXIlH2GDd8JS1j6zHDUw0aQ"
client = Client()
with open("liste_de_blanc.txt" , "r" , encoding="utf8") as fichier:
    content = fichier.read();
    liste_blanc = content.split("\n")

@client.event
async def on_ready():
    print("The bot is runnig!")
    await client.change_presence(game=Game(name="Jeu du ? BLANC!"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content in liste_blanc:
        await client.send_message(message.channel, "BLANC !")
        await client.send_file(message.channel, "blanc.png")

client.run(token)