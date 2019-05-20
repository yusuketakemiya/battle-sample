import random
from Character import Character

class Yusa(Character):
    def __init__(self):
        super().__init__()
        self.hp = 120
        self.power = 21
        self.name = "勇者"
        self.message = "世界に平和が訪れた。"
    
    def attack(self, character):
        if self.isDeath:
            return
        if (random.randint(1,2) % 2 == 0):
            print("ミス！{}の攻撃が当たらない！".format(self.name))
            return
        super().attack(character)
    