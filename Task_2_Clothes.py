# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:20:26 2020

@author: 1
"""

from abc import ABC, abstractmethod

class Clothes(ABC):
    
    def __init__(self, param):
        self.param = param
        
    @abstractmethod
    def useCloth(self):
        pass

class Coat(Clothes):
    def useCloth(self):
        return round(self.param / 6.5 + 0.5, 2)
    
class Suit(Clothes):
    def useCloth(self):
        return round(self.param * 2 + 0.3,2)

coat_1 = Coat(37)
print(f"Для пошива пальто размера {coat_1.param} нужно {coat_1.useCloth()} метров ткани")

suit_1 = Suit(1.7)
print(f"Для пошива костюма на рост {suit_1.param} метра нужно {suit_1.useCloth()} метров ткани")


    
