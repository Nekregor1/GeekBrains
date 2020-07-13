# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 21:24:29 2020

@author: 1
"""

myList = [7, 5, 3, 3, 2]

print(myList)

solution = "y"
while solution != "" :
    temp = True
    while temp == True:
        try:
            userNumber = int(input("Введите натуральное число "))
            if userNumber < 1:
                print("Вы ввели не натуральное число!")
            else :
                temp = False
        except Exception:
            print("Вы ввели не натуральное число!")
    temp2 = 0

    while userNumber < myList[temp2]:
        temp2 = temp2 + 1
        if temp2 == len(myList) :
            break
    if temp2 == len(myList) :
        myList.append(userNumber)
    else:
        myList.insert(temp2, userNumber)

    print(myList)
    
    solution = input("Не хотите продолжать? Для выхода нажмите Enter ")

    