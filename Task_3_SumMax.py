# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:33:54 2020

@author: 1
"""

def my_func(first, second, third):
    myList = [first, second, third]
    myList.sort() 
    return myList[2] + myList[1]

firstNum = float(input("Введите первое число "))
secondNum = float(input("Введите второе число "))
thirdNum = float(input("Введите третье число "))
   
print(f"Сумма двух наибольших чисел из введенных равна: {my_func(firstNum, secondNum, thirdNum)}")
