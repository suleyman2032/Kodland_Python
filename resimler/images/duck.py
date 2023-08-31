import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
from aiohttp import request


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = request.get(url)
    data = res.json()
    return data['url']


@bot.command("duck")
async def duck(ctx):
    #'''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run("MTEzNjY5ODE5MjE2ODIzMDkyMg.GZ9Rn4.0zLTTbg9uW1fy0yo7a4_y9C_7WyG6p0I8V5JEI")