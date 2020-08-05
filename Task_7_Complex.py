# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:27:25 2020

@author: 1
"""

class MyComplex:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
        
    def __str__(self):
        if self.Im >= 0:
            return f"{self.Re} + j{self.Im}"
        else:
            return f"{self.Re} - j{abs(self.Im)}"
        
    def __add__(self, other):
        return MyComplex(self.Re + other.Re, self.Im + other.Im)
    
    def __mul__(self, other):
        return MyComplex(self.Re * other.Re - self.Im * other.Im , self.Re * other.Im + self.Im * other.Re)

cpx_1 = MyComplex(1,1)
cpx_2 = MyComplex(-1,-1)
cpx_3 = cpx_1 + cpx_2
cpx_4 = cpx_1 * cpx_2

print(cpx_1)
print(cpx_2)
print(cpx_3)
print(cpx_4)