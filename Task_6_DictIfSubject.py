# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:14:41 2020

@author: 1
"""
import re

myList = []
with open("text_6.txt", "r", encoding="utf-8") as myFile:
    for line in myFile:
        myList.append(line.split())

    
myDict = {}
for myStr in myList:
    name = myStr[0][0:len(myStr[0])-1]
    count = 0
    sumOfLes = 0
    for numWord in range(1, len(myStr)):
        if(len(re.findall(r'[0-9]+', myStr[numWord]))>0):
            sumOfLes = sumOfLes + int(re.findall(r'[0-9]+', myStr[numWord])[0])   
    myDict.update({f"{name}" : sumOfLes})
    
print(f"Получили словарь:\n{myDict}")