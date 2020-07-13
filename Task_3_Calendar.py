# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:37:26 2020

@author: 1
"""
temp = True

while temp == True:
    try:
        month = int(input("Введите номер месяца числом "))
        if month >12 or month < 0:
            print("Введенное число не может быть номером месяца. Введите корректное число")
        else:
            temp = False
    except Exception:
        print("Вы ввели не натуральное число!")

dictCalendar = {1:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна", 6:"Лето", 7:"Лето", 8:"Лето", 9:"Осень", 10:"Осень", 11:"Осень", 12:"Зима"}
listCalendar = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]

print(f"Месяц №{month} принадлежит времени года {dictCalendar.get(month)}")
print(f"Месяц №{month} принадлежит времени года {listCalendar[month-1]}")

