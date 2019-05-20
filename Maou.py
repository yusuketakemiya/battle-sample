import random
from Character import Character

class Maou(Character):
    def __init__(self):
        super().__init__()
        self.hp = 200
        self.power = 10
        self.name = "魔王"
        self.message = "世界は闇に落ちた。"
    
    def attack(self, character):
        if self.isDeath:
            return
        if (random.randint(1,2) % 2 != 0):
            print("ミス！{}の攻撃が当たらない！".format(self.name))
            return
        super().attack(character)
    