# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (600, 600)

x = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]
y = [590, 593, 595, 598, 596, 598, 599, 594, 597, 598, 599, 596, 599, 598, 599, 597, 598, 599, 599, 596]
long = random.randint(10, 20)
background_color = (0, 8, 98)

while True:
    for idx, val in enumerate(x):
        # TODO очень смущает то как отображается результат думаю что неверно.?!
        point = sd.get_point(x[idx], y[idx])
        sd.snowflake(center=point, length=long)
        sd.snowflake(center=point, length=long, color=background_color)
        y[idx] -= random.randint(1, 15)
        if y[idx] < 0:
            y[idx] = 600
            sd.snowflake(center=point, length=long)
        x[idx] += random.randint(-12, 25)
        x[idx] -= random.randint(-12, 25)
        if y[idx] < 20:
            y[idx] = 0
    sd.sleep(0.5)
    if sd.user_want_exit():
        break
sd.pause()
