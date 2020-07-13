# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:41:07 2020

@author: 1
"""

myStr = input("Введите строку ")
myList = myStr.split()

for count in range(len(myList)):
    print(f"{count}: {myList[count][0:9]}")