# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:32:14 2020

@author: 1
"""

with open("text_4.txt", "r", encoding= "utf-8") as myFile:
    myList = []
    myDict = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре", 
              "Five":"Пять", "Six":"Шесть", "Seven":"Семь", "Eight":"Восемь", "Nine":"Девять", "Zero":"Ноль"}
    for line in myFile:
        myList.append(line.split())
    print(myList)
    
    for strInEng in myList:
        for word in range(len(strInEng)):
            if myDict.get(strInEng[word])!=None:
                strInEng[word] = myDict.get(strInEng[word])
    print(myList)
    with open("FileTask_4.txt", "w", encoding= "utf-8") as myFile:
        for el in myList:
            myFile.write(' '.join(el)+"\n")