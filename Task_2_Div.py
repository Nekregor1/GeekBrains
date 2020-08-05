# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:11:28 2020

@author: 1
"""

class myException(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_div1 = input("Введите делимое (действительное число) ")
inp_div2 = input("Введите делитель (действительное число) ")

try:
    inp_div1 = float(inp_div1)
    inp_div2 = float(inp_div2)
    if inp_div2==0:
        raise myException("Вы ввели в качестве делителя ноль! На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число!")
except myException as err:
        print(err)
else:
    print(f"Все хорошо. Частное двух чисел равно: {inp_div1/inp_div2}")