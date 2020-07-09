# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:20:29 2020

@author: 1
"""

revenue = int(input("Введите число-размер выручки компании "))
costs = int(input("Введите число-размер издержек компании "))


if revenue > costs :
    print("Компания работает с прибылью")
    profit = revenue - costs
    print(f"Рентабельность выручки равняется {profit/revenue}")
    staff = int(input("Введите количество сотрудников компании "))
    print(f"Прибыль компании в расчете на одного сотрудника равна {profit/staff} ")
elif revenue == costs :
    print("Компания работает безубыточно")
else :
	print("Компания работает в убыток")

input("\n\nНажмите Enter, чтобы выйти.")

