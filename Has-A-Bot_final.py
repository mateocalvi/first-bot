import discord
import asyncio, functools, itertools, random, youtube_dl, re, os, platform
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from async_timeout import timeout
from urllib import parse, request
from math import cos, radians, sqrt, ceil
from requests import get

#########################################################################################################################################################
########################################################                                  ###############################################################
########################################################     [Orden de los atributos:]    ###############################################################
########################################################     (1.) Eventos                 ###############################################################
########################################################     (2.) Comandos                ###############################################################
########################################################     (3.) Listen's                ###############################################################
########################################################                                  ###############################################################
#########################################################################################################################################################

bot = commands.Bot(command_prefix='<', description='')

@bot.event
async def on_ready():
	bot.loop.create_task(status_task())
	print(f"Conectado como {bot.user.name}")
	print(f"Version de Discord.py API: {discord.__version__}")
	print(f"Version de Python: {platform.python_version()}")
	print(f"Ejecutándose en: {platform.system()} {platform.release()} ({os.name})")
	print("-------------------")
	print("My Ready is Body")
async def status_task():
	while True:
		await bot.change_presence(activity=discord.Streaming(name='Get Rickrolled!', platform='YouTube', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
		await asyncio.sleep(60)
		await bot.change_presence(activity=discord.Game("<help"))
		await asyncio.sleep(60)

invitacion = 'https://discord.com/api/oauth2/authorize?client_id=736328464285696000&permissions=8&scope=bot'

@bot.command()
async def invit(ctx):
        await ctx.send(invitacion)

@bot.command()
async def ping(ctx):
    usuario = str(ctx.author)
    embed = discord.Embed(colour=discord.Colour.dark_purple(), title=usuario + ' Pong!', description='Tardó {0} ms'.format(round(bot.latency, 1)))
    embed.set_thumbnail(url='https://images.emojiterra.com/google/android-nougat/512px/1f3d3.png')
    await ctx.send(embed=embed)
    # print(usuario + 'Pong! {0}ms'.format(round(bot.latency, 1)))

# [Comandos de música (El módulo de música ya no fuinciona)]
# @bot.command()
# async def coms(ctx):
#     embed = discord.Embed(colour=discord.Colour.dark_purple(), title='Comandos', description='Lista de los comandos que este Bot acepta')
#     embed.set_thumbnail(url='https://icons-for-free.com/iconfiles/png/512/checkmark+clipboard+document+list+tracklist+icon-1320167911544323810.png')
#     embed.add_field(name='Comandos de música:', value=None, inline=True)
#     embed.add_field(name='<play (<p)', value='Busca una pista y la reproduce', inline=False)
#     embed.add_field(name='<stop (<st)', value='Detiene el bot y borra la cola de reproducción', inline=False)
#     embed.add_field(name='<skip (<sk)', value='Salta a la siguiente pista', inline=False)
#     embed.add_field(name='<queue (<q)', value='Muestra la cola', inline=False)
#     embed.add_field(name='<loop (<lp)', value='Repite la pista o cola actual', inline=False)
#     embed.set_footer(text='https://discord.com/api/oauth2/authorize?client_id=736328464285696000&permissions=8&scope=bot')
#     await ctx.send(embed=embed)

# Buscar un video en youtube
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen(f'http://www.youtube.com/results?{query_string}')
    #print(html_content.read().decode())
    search_results = re.findall( r'watch\?v=(\S{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Suma de dos números
@bot.command()
async def sum(ctx, *, numbers: int):
    await ctx.send(float(numbers) + float(numbers))

# Teorema de Pitágoras
@bot.command()
async def ptgr(ctx, a1: int, b1: int):
    h1 = sqrt(a1**2 + b1**2)
    await ctx.send(round(float(h1), 2))

# Teorema del coseno
@bot.command()
async def teorem_cos(ctx, a2, b2, alpha):
    h1 = (a2**2 + b2**2 - (2*a2*b2*cos(radians(alpha))))
    h2 = sqrt(h1)
    await ctx.send(round(float(h2), 2))
    await ctx.send(f"(sqrt({h1}))")


# lista de memes
listaMemes = [
    "https://i.imgur.com/iXxawLm.jpg",
    "https://i.imgur.com/NUKAipe.jpg",
    "https://i.imgur.com/Rq6TJyi.jpg",
    "https://i.imgur.com/iEe4ezd.jpg",
    "https://i.imgur.com/fq4ANff.jpg",
    "https://i.imgur.com/8rZ2Hod.jpg",
    "https://i.imgur.com/Hqds7RA.jpg",
    "https://i.imgur.com/YhCyLtl.jpg",
    "https://i.imgur.com/bCBt6ga.jpeg",
    "https://i.imgur.com/0ooelxA.jpeg",
    "https://i.imgur.com/gJ4FQ51.jpeg",
    "https://i.imgur.com/uZ9SUt4.jpeg",
    "https://i.imgur.com/oAChZ9A.jpeg",
    "https://i.imgur.com/WkbkAFv.jpeg",
    "https://i.imgur.com/wGdNHbd.jpeg",
    "https://i.imgur.com/EsTgUcu.jpeg",
    "https://i.imgur.com/7VO7cY6.jpeg",
    "https://i.imgur.com/0LyUhow.jpeg",
    "https://i.imgur.com/mtQOg4k.jpeg",
    "https://i.imgur.com/pzPfY7Q.jpeg",
    "https://i.imgur.com/Qw7GnHq.jpeg",
    "https://i.imgur.com/0CxTCdm.jpeg",
    "https://i.imgur.com/L0a52X3.jpeg",
    "https://i.imgur.com/rkvJE4J.jpeg",
    "https://i.imgur.com/cjEdM7C.jpeg",
    "https://i.imgur.com/k7Tfrbs.jpeg",
    "https://videos1.memedroid.com/videos/UPLOADED452/5f417fa24ce8f.mp4",
    "https://images7.memedroid.com/images/UPLOADED880/5f67a83ee419a.jpeg",
    "https://images7.memedroid.com/images/UPLOADED642/5f664096e7b33.jpeg",
    "https://images7.memedroid.com/images/UPLOADED922/5f33da9038ac2.jpeg",
    "https://images3.memedroid.com/images/UPLOADED166/5f67a74322e2e.jpeg",
    "https://images3.memedroid.com/images/UPLOADED350/5f42f5f40bcfa.jpeg",
    "https://images7.memedroid.com/images/UPLOADED693/5f662dc2f2d9f.jpeg",
    "https://images3.memedroid.com/images/UPLOADED152/5f551e2dc16df.jpeg",
    "https://images7.memedroid.com/images/UPLOADED946/5f43cdb30e080.jpeg",
    "https://images7.memedroid.com/images/UPLOADED807/5f5e8873b3354.jpeg",
    "https://images7.memedroid.com/images/UPLOADED925/5f3d8c8fa2238.jpeg",
]

@bot.command()
async def meme(ctx):
    await ctx.send(random.choice(listaMemes))

# Obtener mi IP pública para conectarse al servidor
# Sólo funciona cuando el archivo se ejecuta de forma local
@bot.command()
async def ip(ctx):
    ip = get('https://api.ipify.org').text
    await ctx.send('La IP del server (Minecraft 1.16.2) es: {}'.format(ip))

bot.run(Token)
