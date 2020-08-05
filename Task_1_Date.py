# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:51:07 2020

@author: 1
"""

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
                
    def __str__(self):
        return f"{self.day} {self.month} {self.year}"
    
    @classmethod
    def extract(cls, data):
        day, month, year = data.split("-")
        day = int(day)
        month = int(month)
        
        return cls(int(day), int(month), int(year))
    
    @staticmethod
    def validation(day, month, year):
        if day > 31:
            print("Колличество дней не может превышать 31!")
        else:
            print("Дата верная!")
        


date_1 = Date.extract("1-12-1990")
print(date_1.validation(Date.extract("1-12-1990")))


