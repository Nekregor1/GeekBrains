# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:19:53 2020

@author: 1
"""

def my_func(x,y):
    return x**y

def my_func2(x,y):
    temp = 1
    for count in range(abs(y)):
        temp = temp/x
    return temp

x = float(input("Введите действительное положительное число "))
y = int(input("Введите целое отрицательное число "))

print(f"Число {x} в степени {y} равно {round(my_func(x,y),10)}")
print(f"Число {x} в степени {y} равно {round(my_func2(x,y),10)}")