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

