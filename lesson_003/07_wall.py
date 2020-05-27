# -*- coding: utf-8 -*-

# (цикл for)
# noinspection PyUnresolvedReferences
import simple_draw as sd

sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

start_left_point_x, start_left_point_y = x, y, = 0, 0
end_right_point_x, end_right_point_y = x1, y1 = 100, 50

step = 600
# todo  не пойму почему наложение происходит ?  степ это переменная для определения количества строк, и цикл под нее
# todo и условие поставил  помоги !!!
for step in range(12):
    if step / 50 % 2 == 0:
        x += 100
        x1 += 100
        y += 50
        y1 += 50
        for x in range(-101, 700, 50):
            for y in range(-51, 700, 50):
                left_point = sd.get_point(x, y)
                right_point = sd.get_point(x1, y1)
                sd.rectangle(left_bottom=left_point, right_top=right_point, color=sd.COLOR_DARK_GREEN, width=2)
    else:
        for x in range(-101, 700, 50):
            x += 50
            x1 += 50
            for y in range(-51, 700, 50):
                y += 0
                y1 += 0
                left_point = sd.get_point(x, y)
                right_point = sd.get_point(x1, y1)
                sd.rectangle(left_bottom=left_point, right_top=right_point, color=sd.COLOR_BLACK, width=2)

sd.pause()
