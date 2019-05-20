import random
from abc import ABCMeta, abstractmethod

class Character(object):
    def __init__(self):
        self.hp = 0
        self.power = 0
        self.isDeath = False
        self.name = ""
        self.message = ""

    def win(self):
        print(self.message)
    
    def lose(self):
        print("{}は倒れた。".format(self.name))
    
    @abstractmethod
    def attack(self, character):
        print("{}の攻撃!".format(self.name))
        power = self.power
        if (random.randint(0,10) == 10):
            print("会心の一撃！")
            power = int(power * 1.5)
        character.damage(power)

    def damage(self, power):
        self.hp = self.hp - power
        self.isDeath = self.hp <= 0
        print("{}に{}のダメージ".format(self.name, power))

    def printStatus(self):
        print("{}：HP:{} 攻撃力:{}".format(self.name, self.hp, self.power))
