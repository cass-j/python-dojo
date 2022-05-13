# !/usr/bin/python3
import random

all_players = []

class Player:

    def __init__(self, name= "New Player", age = 1, race = "Human",height= 5.2, weight= 160,):
        self.id = random.randint(1,1000000)
        self.name = str.title(name)
        self.age = age
        self.race= str.title(race)
        self.height = height
        self.weight = weight
        self.level = 0
        self.money = 100
        self.stats = {
            "strength" : 10,
            "dexterity" : 10,
            "constitution" : 10,
            "intelligence" : 10,
            "perception" : 10,
            "charisma" : 10,
        },
        self.isBanned = False
        self.username= self.name + "#" + str(self.id)

    def ban(self):
        self.isBanned = True

player1 = Player('george',15,'human',4.6,147)
print(player1.username)
# player1.ban()
print(player1.isBanned)

print(f'Hello {player1.name}!')