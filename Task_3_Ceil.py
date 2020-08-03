# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:13:51 2020

@author: 1
"""

class Ceil:
    def __init__(self, ceilCount):
        self.ceilCount = ceilCount
    
    def __str__(self):
        rtr = ""
        for dot in range(self.ceilCount):
            rtr = rtr + "*"
        return rtr
    
    def __add__(self, other):
        return Ceil(self.ceilCount + other.ceilCount)
    
    def __sub__(self, other):
        if self.ceilCount < other.ceilCount:
            print("Нельзя вычитать эти клетки")
            return Ceil(0)
        else:
            return Ceil(self.ceilCount - other.ceilCount)
    def __mul__(self, other):
        return Ceil(self.ceilCount * other.ceilCount)
    
    def __truediv__(self, other):
        return Ceil(self.ceilCount // other.ceilCount)
    
    def make_order(self, ceilInRow):
        rtr = ""
        for dotInRow in (range(self.ceilCount // ceilInRow)):
            temp = "*" * ceilInRow
            rtr = rtr + temp + "\n"
        temp = "*" * (self.ceilCount % ceilInRow)
        rtr = rtr + temp
        print(rtr)

ceil_1 = Ceil(12)
ceil_2 = Ceil(3)

ceil_3 = ceil_1 + ceil_2
print(ceil_3)

ceil_4 = ceil_2 - ceil_1
print(ceil_4)

ceil_5 = ceil_1 * ceil_2
print(ceil_5)

ceil_6 = ceil_1 / ceil_2
print(ceil_6)

ceil_2.make_order(7)
