import networkx as nx
import random
import math

class Memory:
    
    def __init__(self, room, action, valence_delta):
        self.room = room
        self.action = action
        self.valence_delta = valence_delta


class Status:

    def __init__(self):
        self.hunger = 0
        self.thirst = 0
        self.entertainment = 0
        
    def __repr__(self):
        return f"hunger: {self.hunger}, thirst: {self.thirst}, entertainment: {self.entertainment}"

    def get_need(self, value):
        return math.sqrt(value / 3)
        
    def valence(self):
        sum = self.get_need(self.hunger) + self.get_need(self.thirst) + self.get_need(self.entertainment) 
        return sum / 3


class Character:
    
    def __init__(self, name):
        self.name = name
        self.status = Status() 
        self.memories = []

    def update(self, room):
        actions = room.get_actions()
        selected = random.randrange(0, len(actions))
        select_action = list(actions)[selected]
        result = actions[select_action](self.name)
        initial_valence = self.status.valence()
        
        for k, v in result.items():
            if k == "hunger":
                self.status.hunger += v
            if k == "thirst":
                self.status.thirst += v
            if k == "entertainment":
                self.status.entertainment += v

        valence_delta = self.status.valence() - initial_valence
        self.memories.append(Memory(room, select_action, valence_delta))

        print(self.status)
        print(self.status.valence())
        print(len(self.memories))
            
        
        

class Room:

    def eat(self, name):
        print(f"{name} ate food.")
        return {'hunger': 1}

    def drink(self, name):
        print(f"{name} drank water.")
        return {'thirst': 1}

    def read(self, name):
        print(f"{name} read a chapter from a book.")
        return {'entertainment': 1}

    def get_actions(self):
        return { "eat": self.eat,
                 "drink": self.drink,
                 "read": self.read }

def main():
    room = Room()
    character = Character("Mark")
    
    for i in range(0, 4):
        character.update(room) 
    

if __name__ == "__main__":
    main()
