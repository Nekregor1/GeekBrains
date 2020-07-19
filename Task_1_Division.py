# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:00:39 2020

@author: 1
"""

def myDiv(first, second):
    if second == 0:
        return "Ошибка! На ноль делить нельзя!"
    else:
        return f"Частное двух чисел равно: {round(first/second,2)}"
    
firstNum = float(input("Введите первое число "))
secondNum = float(input("Введите второе число "))

print(myDiv(firstNum, secondNum))