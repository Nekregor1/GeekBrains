# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:07:30 2020

@author: 1
"""

def fact(n):
    res = 1
    for el in range(1, n+1):
        res = res * el
        yield res

for el in fact(10):
    print(el)
