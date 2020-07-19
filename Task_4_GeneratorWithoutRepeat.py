# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:25:20 2020

@author: 1
"""

myOldList =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

listWithoutRepeat = [el for el in myOldList if myOldList.count(el)==1]

print(myOldList)
print(listWithoutRepeat)