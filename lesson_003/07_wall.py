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
    if (y / 50) % 2 == 0 in range(50):
        x = x_shift
        x1 = x1_shift
        y += 50
        y1 += 50
    elif (y / 50) % 2 == 1 in range(50):
        x += 100
        x1 += 100
        y += 50
        y1 += 50
        # TODO тут наверное надо range делать от вычисленного х или shift.
    for x in range(0, 700, 100):
        left_point = sd.get_point(x, y)
        # TODO тут скорее не x1, а x + 100
        right_point = sd.get_point(x1, y1)
        print(left_point, right_point) # TODO вот я распринтил точки, посмотри, мб наведут на мысль.
        sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
sd.pause()

