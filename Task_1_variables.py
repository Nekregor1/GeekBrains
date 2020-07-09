# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:23:46 2020

@author: 1
"""

var_num_1 = 10
var_text_1 = 'Маша'
var_num_2 = int(input("Введите число "))
var_text_2 = input("Введите строку ")

var_num_3 = var_num_1 + var_num_2
var_text_3 = var_text_1 + var_text_2

print(f"Сумма введенного числа и 10 равна {var_num_3}")
print("\nЕсли приписать справа к слову 'Маша' введенную строку, то получится %s" % var_text_3)

input("\n\nНажмите Enter, чтобы выйти.")