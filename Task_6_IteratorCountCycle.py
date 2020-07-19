# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:45:20 2020

@author: 1
"""

from itertools import count
from itertools import cycle


def iteratorStartNum(start):
    for el in count( start ):
        if el > 10 :
            break
        else :
            print(el)


def iterationCycle(string):
    с = 0
    for el in cycle( string ):
        if с > 10 :
            break
        print(el)
        с += 1        

iteratorStartNum(5)

iterationCycle("Ahahah")