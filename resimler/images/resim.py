import discord
import random
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def mem(ctx):
    with open(r'C:\Users\Sahip\Desktop\Kodland_Python\resimler\images\mem1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def randommem(ctx):
    
    img_name = random.choice(os.listdir(r"C:\Users\Sahip\Desktop\Kodland_Python\resimler\images"))
    with open(f'resimler\images\{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
print(os.listdir(r'C:\Users\Sahip\Desktop\Kodland_Python\resimler\images'))
bot.run("MTEzNjY5ODE5MjE2ODIzMDkyMg.GZ9Rn4.0zLTTbg9uW1fy0yo7a4_y9C_7WyG6p0I8V5JEI")

