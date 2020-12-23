# -*- coding: utf-8 -*-

import simple_draw as sd
import random


def sno():
    sd.resolution = (1200, 600)
    x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
    y = [590, 593, 595, 598, 596, 598, 599, 594, 597, 598, 599, 596, 599, 598, 599, 597, 598, 599, 599, 596]
    long = random.randint(3, 8)
    background_color = (0, 8, 98)

    while True:
        for idx, val in enumerate(x):
            point = sd.get_point(x[idx], y[idx])
            sd.snowflake(center=point, length=long, color=background_color)
            y[idx] -= random.randint(0, 20)

            point = sd.get_point(x[idx], y[idx])
            sd.snowflake(center=point, length=long)
            if y[idx] < 20:
                y[idx] = 600
        if sd.user_want_exit():
            break
    return


if __name__ == '__main__':
    sd.pause()
