import aiohttp
import random

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.img = None
        self.name = None

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['forms'][0]['name']
                else:
                    return "Pikachu"

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
        return f"Имя твоего покемона: {self.name}"

    async def show_img(self):
        url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.pokemon_number}.png"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    # Читаем данные изображения в память
                    data = await resp.read()
                    return data
                else:
                    return None