# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:51:23 2020

@author: 1
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        print("Машина поехала")
        
    def stop(self):
        print("Машина остановилась")
        
    def turn(self, direction):
        print(f"Машина повернула {direction}")
    
    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}")
        
class TownCar(Car):
    LIMIT_SPEED = 60
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)    
    def show_speed(self):
        if self.speed > self.LIMIT_SPEED:
            print("Вы превысили максимально допустимую скорость!")
        else:
            print(f"Текущая скорость автомобиля {self.speed}")

class WorkCar(Car):
    LIMIT_SPEED = 40 
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)  
    def show_speed(self):
        if self.speed > self.LIMIT_SPEED:
            print("Вы превысили максимально допустимую скорость!")
        else:
            print(f"Текущая скорость автомобиля {self.speed}")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
    
townCar1 = TownCar(61, "blue", "Lada")
townCar1.show_speed()
townCar1.turn("Направо")

sportCar1 = SportCar(100, 'red', 'Ferrari')
sportCar1.show_speed()
sportCar1.turn("Направо")

policeCar1 = PoliceCar(80, 'white', 'Ford')
policeCar1.show_speed()
policeCar1.turn("Направо")

workCar1 = WorkCar(37, 'yellow', 'bmw')
workCar1.show_speed()
workCar1.turn("Направо")