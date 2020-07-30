# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:25:24 2020

@author: 1
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        
        
class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника {self.name} {self.surname}")
        
    def get_total_income(self):
        temp = self._income.get("wage") + self._income.get("bonus")
        print(f"Полный доход сотрудника с учетом премии {temp}")

worker_1 = Position('Egor', 'Nekrasov', 'engineer', 100000, 30000)
worker_1.get_full_name()
worker_1.get_total_income()