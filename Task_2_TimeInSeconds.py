# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:09:08 2020

@author: 1
"""

timeInSec = int(input("Введите время в секундах "))

timeHour = timeInSec // 3600
temp = timeInSec % 3600
timeMinute =  temp // 60
timeSecond = temp % 60
 
print(f"В классическом представлении времени это будет выглядеть: {timeHour}:{timeMinute}:{timeSecond}")

input("\n\nНажмите Enter, чтобы выйти.")