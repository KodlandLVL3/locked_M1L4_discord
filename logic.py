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
        # Асинхронный метод для получения URL изображения покемона через PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:  # Открытие сессии HTTP
            async with session.get(url) as response:  # Отправка GET запроса на получение данных о покемоне
                if response.status == 200:
                    data = await response.json()  # Получение JSON ответа
                    img_url = data['sprites']['front_default']  # Получение URL покемона
                    return img_url  # Возвращаем URL изображения
                else:
                    return None  # Возврат None, если запрос не удался
