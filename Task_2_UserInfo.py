# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:17:52 2020

@author: 1
"""

def myPrintInfo(surname, name, year, city, email):
    print(f"{surname} {name} родился в {year} году. Проживает в городе {city}. Электронный адрес: {email}")

Users = {"name": ["Иван"], "surname": ["Иванов"], "year": [2000], "city": ["Москва"], "email": ["ivanov@mail.ru"]}

myPrintInfo(name = Users.get("name")[0], surname = Users.get("surname")[0], year = Users.get("year")[0], city = Users.get("city")[0], email = Users.get("email")[0])
