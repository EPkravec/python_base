# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

x, y, = 0, 0
x1, y1 = 100, 50
x_shift, y_shift, = -50, 50
x1_shift, y1_shift = 50, 100

for y in range(0, 700, 50):
    if (y / 50) % 2 == 1:
        for x in range(0, 700, 100):
            left_point = sd.get_point(x_shift, y_shift)
            right_point = sd.get_point(x1_shift, y1_shift)
            x_shift = -50
            x1_shift = 50
            y_shift += 100
            y1_shift += 100
            print(left_point, right_point)
            sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
    if (y / 50) % 2 == 0:
        for x in range(0, 700, 100):
            left_point = sd.get_point(x, y)
            right_point = sd.get_point(x1, y1)
            x = 0
            x1 = 100
            y = 0
            y1 += 50
            print(left_point, right_point)
            sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)

sd.pause()

# todo вот что то более менее получаеться но  не могу понять пока что именно нужно с координатами делать
#  Я принты поставил, мб натолкнет на мысль, посмотри, если не получится помогу
