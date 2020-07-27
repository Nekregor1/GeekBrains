# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:18:41 2020

@author: 1
"""

import statistics

with open("text_3.txt", "r", encoding= "utf-8") as myFile:
    listWorker = []
    for line in myFile:
        listWorker.append(line.split())

    bigSalList = []
    bigSalList = [el for el in listWorker if float(el[1]) >= 20000]
    
    print("Работники с зарплатой не менее 20000:")
    numOfWorker = 1
    for el in bigSalList:
        print(f"{el[0]} c зарплатой {el[1]}")
        numOfWorker = numOfWorker + 1
    meanSal = statistics.mean([float(el[1]) for el in listWorker ])
    print (f"Средняя зарплата всех сотрудников равна: {meanSal}")