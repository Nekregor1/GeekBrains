# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:12:41 2020

@author: 1
"""

oldList = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 56]

newList = [oldList[count] for count in range(1, len(oldList)) if oldList[count]>oldList[count-1]]

print(oldList)
print(newList)
