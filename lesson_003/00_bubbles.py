# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (255, 0, 0)
sd.caption = 'circle lesson № 3'

point = sd.get_point(100, 100)
radius = 50
color = sd.COLOR_BLACK
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, color=color)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bublle (point, step):
    radius = 50
    color = sd.COLOR_BLUE
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)

point = sd.get_point(100, 100)
bublle(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
# Нарисовать три ряда по 10 пузырьков
for y in range(100, 601, 200):
    for x in range(100, 1201, 120):
        point = sd.get_point(x, y)
        bublle(point=point, step=10)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    step_1 = random.randint(1, 10)
    point = sd.random_point()
    color = sd.random_color()
    bublle(point=point, step=step_1)
    sd.circle(center_position=point, radius=radius, color=color, width=2)

sd.pause()
