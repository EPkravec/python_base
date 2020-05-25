# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (255, 0, 0)
sd.caption = 'circle lesson № 3'

#  1 задание

point = sd.get_point(100, 100)
radius = 50
color = sd.COLOR_BLACK
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, color=color)

sd.sleep(3)

# 2 задание
sd.clear_screen()

def bublle (point, step):
    radius = 50
    color = sd.COLOR_BLUE
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)

point = sd.get_point(100, 100)
bublle(point=point, step=10)

for y in range(100, 601, 200):
    for x in range(100, 1201, 120):
        point = sd.get_point(x, y)
        bublle(point=point, step=10)

sd.sleep(3)

# 3 задание
sd.clear_screen()

for _ in range(100):
    step_1 = random.randint(1, 10)
    point = sd.random_point()
    color = sd.random_color()
    bublle(point=point, step=step_1)
    sd.circle(center_position=point, radius=radius, color=color, width=2)

sd.pause()

# зачет!
