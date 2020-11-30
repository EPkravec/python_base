# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (600, 600)

x = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]  
y = [550, 540, 530, 540, 550, 560, 545, 530, 500, 560, 550, 540, 530, 540, 550, 560, 545, 530, 500, 560]
long = random.randint(10, 20)


while True:
    sd.clear_screen()
    for idx, val in enumerate(x):
        point = sd.get_point(x[idx], y[idx])
        sd.snowflake(center=point, length=long)
        y[idx] -= random.randint(20, 50)
        x[idx] += random.randint(12, 25)
        x[idx] -= random.randint(12, 25)
        if y[idx] < 2: # TODO тут молодец, но сделай, чтобы оставался сугроб, то есть чтобы перед поднятием снежинка последний раз отрисовалась внизу и всё.
            y[idx] = 600
        elif y[idx] < 50:
            for idx, val in enumerate(x):
                point = sd.get_point(x[idx], y[idx])
                sd.snowflake(center=point, length=long)
    sd.sleep(0.3)
    if sd.user_want_exit():
        break
sd.pause()

