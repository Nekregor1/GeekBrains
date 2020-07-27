# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:57:35 2020

@author: 1
"""

with open("FileTask_5.txt", "a", encoding= "utf-8") as myFile:
    myFile.truncate(0)

while(True):
    with open("FileTask_5.txt", "a", encoding= "utf-8") as myFile:
        inpNum = str(input("Введите число. Для завершения ничего не вводите и нажмите Enter: "))
        if inpNum == "": 
            break
        myFile.write(inpNum + " ")
        
        
with open("FileTask_5.txt", "r", encoding= "utf-8") as myFile:
    numList = [float(num) for num in (myFile.read()).split()]
    numSum = sum(numList)
    print (f"Сумма всех чисел равна: {round(numSum,3)}")