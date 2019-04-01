from discord import *

token = "NTYyMzU0NjAwNDk4NDI5OTc5.XKJlXw.32K4BXIlH2GDd8JS1j6zHDUw0aQ"
client = Client()

liste_blanc = ["Riz" , "riz" , "Mariage" , "mariage" , "Vin" , "vin" , "Requin" , "requin" , "Laurent" , "laurent" , 
"Le Paradis" , "le paradis" , "Michel" , "michel" , "Fromage" , "fromage" , "Marine LePen aime que les" , "marine lepen aime que les",
"Boudin" , "boudin" , "Chocolat" , "chocolat" , "Vote" , "vote" , "Gandalf Le" , "gandalf le" , "Balle à" , "balle à" , "Croc" , "croc" ,
"Cheval" , "cheval" , "Chevalier" , "chevalier" , "Haricot" , "haricot" , "Céleri" , "celeri" , "céleri" , "Celeri" , "Drapeau" , "drapeau" ,
"Mont" , "mont" , "Rasé a" , "Rase a" , "rasé a" , "rase a" , "Sable" , "sable" , "Poivre" , "poivre"]

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

client.run(token)