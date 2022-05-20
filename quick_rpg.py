# !/usr/bin/python3
import random

all_players = []

class Player:

    @staticmethod
    def idNum():
        # generate_users
        userId = random.randint(1,1000000)
        for player in all_players:
            if all_players[player]:
                pass
        return userId

    def __init__(self, name, age = 10):
        self.name = str.title(name)
        self.age = age
        self.isBanned = False
        self.username= (f'{self.name} #{Player.idNum()}')
        self.charCount = 0
        self.char = []


    def account_info(self):
        print(f'Username: {self.username}')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Banned: {self.isBanned}')

    def ban(self):
        self.isBanned = True

    def newChar(self, name, race, height, weight):
        if self.char[self.charCount]:
            self.charCount += 1
        self.char[self.charCount] = Character(name, race, height, weight)
        

class Character:

    def __init__(self, name, race = 'Human', height= 5.2, weight= 160):
        self.name = str.title(name)
        self.race= str.title(race)
        self.height = height
        self.weight = weight
        self.level = 0
        self.money = 100
        self.stats = {
            'strength' : 10,
            'dexterity' : 10,
            'constitution' : 10,
            'intelligence' : 10,
            'perception' : 10,
            'charisma' : 10,
        }
        self.equipment = {
            'hat' : 'none',
            'shirt' : 'none',
            'gloves' : 'none',
            'pants' : 'none',
            'shoes' : 'none',
            'weapon 1' : 'none',
            'weapon 2' : 'none',
            'accessory 1' : 'none',
            'ring 1' : 'none',
            'ring 2' : 'none',
            'misc' : 'none',
        }


# Begin execution
# 
user1 = Player('george forman')
user1.account_info()
user1.newChar('Dilbo', 'hobbit', 3.8, 90)

# print(user1.char[0].name)
# player1 = Player('george',15,'human',4.6,147)
# print(player1.username)
# player1.ban()
# print(player1.isBanned)

# print(f'Hello {player1.name}!')