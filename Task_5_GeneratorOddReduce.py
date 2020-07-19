# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:34:29 2020

@author: 1
"""

from functools import reduce

def multiplication(res, el):
    return res * el

print(reduce(multiplication, [count for count in range(100, 1001) if count % 2 == 0]))

