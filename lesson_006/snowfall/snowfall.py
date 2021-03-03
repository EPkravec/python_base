# -*- coding: utf-8 -*-

import simple_draw as sd
import random

N = 20
color_snow = sd.COLOR_RED

point_1 = {x + 1: {y: random.randint(100, 600) for y in 'xy'} for x in range(N)}
sd.resolution = (600, 600)
long = random.randint(10, 20)
background_color = (0, 8, 98)

x = []
y = []
number_point = []


for key, coordinate in point_1.items():
    for key1 in coordinate:
        if key1 == 'x':
            x.append(point_1[key][key1])
        if key1 == 'y':
            y.append(point_1[key][key1])

while True:
    for idx, val in enumerate(x):
        point = sd.get_point(x[idx], y[idx])
        sd.snowflake(center=point, length=long, color=background_color)
        y[idx] -= random.randint(5, 15)
        x[idx] += random.randint(-10, 10)
        point = sd.get_point(x[idx], y[idx])
        sd.snowflake(center=point, length=long, color=color_snow)
        if y[idx] < 20:
            y[idx] = 600
            x[idx] = random.randint(10, 600)
            for number_snow, coordinate in point_1.items():
                print(f'{number_snow}')

    if sd.user_want_exit():
        break
sd.pause()

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
# while True:
#  нарисовать_снежинки_цветом(color=sd.background_color)
#  сдвинуть_снежинки()
#  нарисовать_снежинки_цветом(color)
#  если есть номера_достигших_низа_экрана() то
#       удалить_снежинки(номера)
#       создать_снежинки(count)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()
