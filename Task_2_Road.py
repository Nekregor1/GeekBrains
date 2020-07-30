# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:05:55 2020

@author: 1
"""

class Road:
    DENSITY = 25        # кг/м3
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def calc(self, thickness):
        weight = self.DENSITY * self._length * self._width * thickness / 1000
        return weight

road_1 = Road(20, 5000)
print(f"{road_1.calc(5)} т")

