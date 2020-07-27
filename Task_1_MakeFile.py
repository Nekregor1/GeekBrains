# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:39:44 2020

@author: 1
"""

while(True):
    with open("FileTask_1.txt", "a", encoding='utf-8') as myFile:
        inputStr = str(input("Введите строку. Для завершения работы введите пустую строку и нажмите Enter\n"))
        if inputStr == "": 
            break
        myFile.write(inputStr + "\n")