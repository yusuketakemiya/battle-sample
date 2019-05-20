from Yusa import Yusa
from Maou import Maou

class Battle(object):
    def __init__(self):
        self.yusa = Yusa()
        self.maou = Maou()
        print("戦闘開始!")
    
    def attack(self):
        self.yusa.printStatus()
        self.maou.printStatus()
        self.yusa.attack(self.maou)
        self.maou.attack(self.yusa)
        
    def next(self):
        return self.maou.isDeath != True and self.yusa.isDeath != True

    def end(self):
        if(self.yusa.isDeath):
            self.yusa.lose()
            self.maou.win()
        else:
            self.maou.lose()
            self.yusa.win()