import discord
import random
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=commands.when_mentioned, description="Nothing to see here!", intents=intents)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)




bot.run("")
