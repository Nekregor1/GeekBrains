# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:53:07 2020

@author: 1
"""

def int_func(magicStr):
    return magicStr.title()

myStr = input("Введите строку, состоящую из латинских букв в нижнем регистре. Или мы самостоятельно переведем её в нижний регистр\n")
#myStr = "tyauf ghjso HJN ddd"
print(f"\nВведенная строка в нижнем регистре:\n{myStr.lower()}\n")

myStrTitle = ""
for el in myStr.split():
    el = int_func(el)
    myStrTitle = myStrTitle + el + " "

print(f"Введенная строка, в которой каждое слово начинается с заглавной буквы:\n{myStrTitle}\n")
