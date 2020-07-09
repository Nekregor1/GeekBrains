# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:44:14 2020

@author: 1
"""

startDist = float(input("Введите стартовый результат спортсмена в км "))
GoalDist = float(input("Введите целевой результат спортсмена в км "))
days = 1            
distance = startDist
#print(f"{days}-й день: {distance}")

while distance < GoalDist:
    distance = distance * 1.1
    days = days + 1
    #print(f"{days}-й день: {distance}")
    
print(f"На {days}-й день спортсмен пробежит более {GoalDist} км")


input("\n\nНажмите Enter, чтобы выйти.")