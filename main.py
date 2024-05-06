import discord
from discord.ext import commands
from config import token 
from logic import Pokemon
from discord import File
from io import BytesIO

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def go(ctx):
    author = ctx.author.name
    if author not in Pokemon.pokemons.keys():
        pokemon = Pokemon(author)
        await ctx.send(await pokemon.info())
        image_data = await pokemon.show_img()
        if image_data:
            image_stream = BytesIO(image_data)
            image_stream.seek(0)
            await ctx.send(file=File(fp=image_stream, filename='pokemon.png'))
        else:
            await ctx.send("Не удалось загрузить изображение покемона.")
    else:
        await ctx.send("Ты уже создал себе покемона.")

@bot.command()
async def start(ctx):
    await ctx.send("Привет! Я бот для игры в покемонов, скорее попробуй создать себе покемона, нажимай - !go")

bot.run(token)
