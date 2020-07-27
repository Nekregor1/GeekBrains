# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:38:36 2020

@author: 1
"""

import json

myList = []
with open("text_7.txt", "r", encoding="utf-8") as myFile:
    for line in myFile:
        myList.append(line.split())
    print(myList)

firmDict = {}
sumProf = 0 
numProf = 0
for word in myList:
    profit = float(word[2])-float(word[3])
    firmDict.update({f"{word[0]}":profit})
        
print(firmDict)


meanProf = sum([word for word in firmDict.values() if float(word) >= 0])/len([word for word in firmDict.values() if float(word) >= 0])
profDict = {"average_profit": round(meanProf,2)}
print(profDict)

with open("my_file_7.json", "w", encoding="utf-8") as write_f:
    json.dump([firmDict, profDict], write_f, ensure_ascii=False)