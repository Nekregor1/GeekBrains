# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:13:33 2020

@author: 1
"""

#myStrOfNum = "1 2 3 4 5 t 6 7 8 9"

myStrOfNum = input("Введите строку чисел, разделенных пробелом\nДля выхода из программы введите не число, а букву\n")
myListOfNum = myStrOfNum.split()

sumOfNum = 0
try:
    el = float(myListOfNum[0])
except Exception:
    print(f"Вы не ввели ни одного числа до 'стоп-символа'! Сумма равна {sumOfNum}")

while type(el) != type("type"):
    for el in myListOfNum:
        try:
            el = float(el)
            sumOfNum += el
        except Exception:
            break
    print(f"Сумма введенных чисел равна {sumOfNum}")
    if type(el) != type("type"):
        myStrOfNum = input("Введите строку чисел, разделенных пробелом\nДля выхода из программы введите не число, а букву\n")
        myListOfNum = myStrOfNum.split()
    else:
        pass

input(f"\nПрограмма завершена. Сумма на момент завершения программы {sumOfNum} Для выхода нажмите Enter")
