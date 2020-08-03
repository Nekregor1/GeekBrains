# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:03:35 2020

@author: 1
"""

class Matrix:
    def __init__(self, listOfLists):
        self.listOfLists = listOfLists
    def __str__(self):
        rtr = ""
        for lists in self.listOfLists:
            for num in lists:
                rtr = rtr + (f"{num} ")
            rtr = rtr + "\n"
        return rtr
    def __add__(self, other):
        rtr = []
        for listsCount in range(len(self.listOfLists)):
            rtr.append([])
            for numCount in range(len(self.listOfLists[listsCount])):
                rtr[listsCount].append(self.listOfLists[listsCount][numCount] + other.listOfLists[listsCount][numCount])
        return Matrix(rtr)


A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]


matrix_A = Matrix(A)
matrix_B = Matrix(B)
print(matrix_A)
print(matrix_B)

matrix_C = matrix_A + matrix_B
print(matrix_C)