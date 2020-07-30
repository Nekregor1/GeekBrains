# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:50:48 2020

@author: 1
"""

class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print("Запуск отрисовки")
        
class Pen(Stationery):
    def __init__(self):
        super().__init__("РУЧКА")
    def draw(self):
        print(f"Каляка-маляка {self.title}")

class Pencil(Stationery):
    def __init__(self):
        super().__init__("КАРАНДАШ")
    def draw(self):
        print(f"Аккуратно нарисовано {self.title}") 

class Handle(Stationery):
    def __init__(self):
        super().__init__("МАРКЕР")
    def draw(self):
        print(f"Шедевр написан {self.title}")
        

pen1 = Pen()
pen1.draw()

pencil1 = Pencil()
pencil1.draw()

handle1 = Handle()
handle1.draw()
