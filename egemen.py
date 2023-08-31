import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
       print(f'{bot.user} Ok Ok I am here! :) ')
    

@bot.command()
async def hello(ctx):
      await ctx.send(f'Hi I am a discord bot and my name is {bot.user}, I can do pretty much everything such as;')
      await ctx.send(f'Tell you about this beatiful game. What is it about , how can you play it and more!!!')
      await ctx.send(f'If you want to have a chat with me you can do that anytime if you want write /chat to the chat!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTEzNjY5ODE5MjE2ODIzMDkyMg.GWqjR6.wrcB1JlfKfDbphqkHiUSqQj2XACICkl1rk-A18")



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'You are finaly here :) Mr/Ms  {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Thank you for joining!(ı reallyapritiate it:)) {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('')
