# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:23:13 2020

@author: 1
"""

import colorama
import time
from colorama import Fore, Back, Style


colorama.init()


class TrafficLight:
    __color = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.YELLOW]
    
    def running(self, timeWork):
        temp = 0
        while temp < timeWork:
            print(TrafficLight.__color[0] + "Красный")
            time.sleep(7)
            temp = temp + 7
            print(TrafficLight.__color[1] + "Желтый")
            time.sleep(2)
            temp = temp + 2
            print(TrafficLight.__color[2] + "Зеленый")
            time.sleep(7)
            temp = temp + 7
            print(TrafficLight.__color[3] + "Желтый")
            time.sleep(2)
            temp = temp + 2

timeTrafficLight = int(input("Введите время работы светофора в секундах: "))
TrafficLight().running(timeTrafficLight)
print(Style.RESET_ALL)
print("Работа программы завершена")
