# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:04:20 2020

@author: 1
"""

with open("FileTask_2.txt", "r", encoding='utf-8') as myFile:
    numOfStr = 0
    for line in myFile:
        numOfStr = numOfStr + 1
        numOfWord = len(line.split())
        if numOfWord ==1:
            print(f"В строке {numOfStr} найдено {numOfWord} слово")
        elif numOfWord > 1 and numOfWord < 5:
            print(f"В строке {numOfStr} найдено {numOfWord} слова")
        else:
            print(f"В строке {numOfStr} найдено {numOfWord} слов")
    
    print(f"В файле найдено {numOfStr} строк")