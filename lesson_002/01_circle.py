#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

pi = 3.1415926
s = radius ** 2 * pi
print(round(s, 4))
# почему не возможно в данном случае использовать s = s.tofised(4) ? да и не полчается
# - Нельзя потому, что в python нет такой ф-ии), в js есть. Ты сделал правильно
# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

point = {
    'point_1': (23, 34),
    'point_2': (30, 30)
}
distanse = dict()
point_1 = point['point_1']
point_2 = point['point_2']

radius_for_point_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
radius_for_point_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
# TODO немогу согласиться с Вами так как точка более 42 единиц, по замечанию дописал изменение >=,
# TODO но в задании нет контретных указаний о том какая переменная (radius point 1 end point 2) должна быть целая или дробная
print(radius >= radius_for_point_1)
print(radius >= radius_for_point_2)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.


# Пример вывода на консоль:
#
# 77777.7777
# False
# False
