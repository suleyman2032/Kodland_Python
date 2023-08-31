import discord
import random

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

def zar_atma():
    zar = random.randint(0, 5)
    if zar == 0:
        return "1"
    elif zar == 1:
        return "2"
    elif zar == 2:
        return "3"
    elif zar == 3:
        return "4"
    elif zar == 4:
        return "5"
    else:
        return"6"



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTEzNjY5ODE5MjE2ODIzMDkyMg.GWqjR6.wrcB1JlfKfDbphqkHiUSqQj2XACICkl1rk-A18")