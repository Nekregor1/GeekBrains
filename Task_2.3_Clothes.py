# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:18:09 2020

@author: 1
"""

class Clothes:
    
    def __init__(self, param):
        self.param = param
        

class Coat(Clothes):
    @property
    def useCloth(self):
        return round(self.param / 6.5 + 0.5, 2)

class Suit(Clothes):
    @property
    def useCloth(self):
        return round(self.param * 2 + 0.3,2)
    

coat_1 = Coat(37)
print(f"Для пошива пальто размера {coat_1.param} нужно {coat_1.useCloth} метров ткани")

suit_1 = Suit(1.7)
print(f"Для пошива костюма на рост {suit_1.param} метра нужно {suit_1.useCloth} метров ткани")