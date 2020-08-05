# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

x, y, = 0, 0

for y in range(0, 700, 50):
    if (y / 50) % 2 == 1:
        for x in range(0, 700, 100):
            left_point = sd.get_point(x, y)
            right_point = sd.get_point(x + 100, y + 50)
            sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
    if (y / 50) % 2 == 1:
        for x in range(0, 700, 100):
            left_point = sd.get_point(x - 50, y + 50)
            right_point = sd.get_point(x + 50, y + 100)
            sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
sd.pause()
