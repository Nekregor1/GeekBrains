# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 19:34:45 2020

@author: 1
"""

myList = list()
el = input("Введите элементы списка. Для прекращения нажмите Enter ")
while el != "":
    myList.append(el)
    el = input("Введите ещё один элемент списка. Для прекращения нажмите Enter ")

if el == "" and len(myList)==0:
    print("Вы ничего не ввели! Программа завершена.")
else:
    print("Введенный список выглядит следующим образом:")
    print(myList)
    if len(myList)<2:
        print("Список слишком короткий, недостаточно элементов для перестановки.")
    else:
        count = 0
        while count < len(myList)-1:
            myList[count+1], myList[count] = myList[count], myList[count+1]
            count = count + 2
        print("После перестановки список будет выглядеть следующим образом:")
        print(myList)

