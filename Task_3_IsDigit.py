# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:25:32 2020

@author: 1
"""

class myException(Exception):
    def __init__(self, txt):
        self.txt = txt

myList = []
while(True):
    try:
        newElement = input("Введите следующий элемент списка: ")
        if newElement.lower() == "stop":
            break
        if newElement.isdigit() == False:
            raise myException("Введенная стока не является числом!")
        myList.append(int(newElement))
    except myException  as err:
        print(err)
print (f"Cписок: {myList}")