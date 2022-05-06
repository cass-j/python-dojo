# !/usr/bin/python3
import random

players = {
    "id0": {
        'name': "New Player",
        'age': 0,
        'race': "Human",
        'height-ft': 5.2,
        'weight-lbs': 160,
        'level': 1,
        'money': 100,
        'isBanned':False,
    }
}
Class Player():

    def initialize():
        playerID = random.randint(1,1000000)
        players[playerID] = {
            'name': "New Player",
            'age': 0,
            'race': "None",
            'height-ft': 0,
            'weight-lbs': 0,
            'level': 0,
            'money': 100,
            'isBanned':False,
        }
        return playerID

    def new_player(name, age, race, height, weight):
        playerID = initialize()
        players[playerID].update(  {
            'name': name,
            'age': age,
            'race': race,
            'height-ft': height,
            'weight-lbs': weight,
        }
        )
        print(f'{players}')

new_player('John',15,'Human',4.6,147)

