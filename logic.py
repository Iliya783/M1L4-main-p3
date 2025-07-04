from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.last_feed_time = datetime.now()
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(900, 1100)
        self.power = randint(100, 150)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu" 
        pass

    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu" 


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name} hp: {self.hp} power: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    

    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer} осталось hp {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"


class Fighter(Pokemon):

    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp -= randint(100, 200)
        self.power += randint(100, 200)
        self.name += " Fighter"

    


class Wizard(Pokemon):

    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp -= randint(100, 200)
        self.power += randint(50, 100)
        self.name += " Wizard"


    def info(self):
        return f"""Имя твоего покеомона: {self.name}
    Cила покемона: {self.power}
    Здоровье покемона: {self.hp}"""


