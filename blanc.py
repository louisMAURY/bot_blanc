import discord

token = "NTYyMzU0NjAwNDk4NDI5OTc5.XKJlXw.32K4BXIlH2GDd8JS1j6zHDUw0aQ"
client = discord.Client()
with open("liste_de_blanc.txt" , "r" , encoding="utf8") as fichier:
    contenu = fichier.read()
    liste_blanc = contenu.split("\n")

@client.event
async def on_ready():
    print("Prêt à combler les blanc !")
    await client.change_presence(game=discord.Game(name="Jeu du ? BLANC!"))

@client.event
async def on_message(message):
    message_utilisateur = message.content.lower()

    if message.author == client.user:
        return
    if message_utilisateur.endswith(tuple(liste_blanc)):
        await client.send_message(message.channel, "BLANC !")
        await client.send_file(message.channel, "blanc.png")

client.run(token)