# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 16:30:34 2020

@author: 1
"""

def calcSalary(rate, hour, bonus):
   salary = rate * hour + bonus
   return salary

myRate = 1000
myHour = 160
myBonus = 100000

print(calcSalary(myRate, myHour, myBonus))
