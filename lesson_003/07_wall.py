# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

start_left_point_x, start_left_point_y = x, y, = 0, 0
end_right_point_x, end_right_point_y = x1, y1 = 100, 50

for x in range(-101, 700, 100):
    x += 100
    x1 += 100
    for y in range(-51, 700, 50):
        y += 50
        y1 += 50
        left_point = sd.get_point(x, y)
        right_point = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
sd.pause()

# todo  сделал обычную кладку