import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptik')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def yardim(ctx):
    await ctx.send(f'size hangi konuda yardım edebilirim:menu yaz')
   
    @bot.command()
    async def menu(ctx):
        with open(r'C:\Users\Sahip\Desktop\Kodland_Python\resimler\images\su.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        await ctx.send(file=picture)
        
        await ctx.send(f'bilgi almak için b,zararları öğrenmek için z`yi seçin.')
            
        @bot.command()
        async def b(ctx):
            await ctx.send(f' hava,su,toprak?.')    

            @bot.command()
            async def hava(ctx):
                await ctx.send(f'kokusu ve rengi yoktur ama hissedilebilir,insanların yaşaması için gereklidir.')
            @bot.command()
            async def su(ctx):
                await ctx.send(f'kokusu yoktur ama  rengi şeffaftır ve hissedilebilir.Tüm  canlıların yaşaması için gereklidir. ')
            @bot.command()
            async def toprak(ctx):
                await ctx.send(f'Ürünlerin ve bitkilerin yetişmesi için çok önemlidir.çeşitli faydalı elementler içerir.')

        @bot.command()
        async def z(ctx):
            await ctx.send(f' havaz,suz,toprakz?.') 
            @bot.command()
            async def havaz(ctx):
                await ctx.send(f'karbon salınımı havayı çok kirletmektedir.')
            @bot.command()
            async def suz(ctx):
                await ctx.send(f'fabrika atıkları ve kimyasal maddeler suyu kirletir. ')
            @bot.command()
            async def toprakz(ctx):
                await ctx.send(f'bazı yerlerde fabrikalar atıklarını toprağa atarak zarar verebilirler.')


bot.run("")
