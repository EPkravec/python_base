# -*- coding: utf-8 -*-

import simple_draw as sd


def homme(x, y):

    for row, y in enumerate(range(0, 250, 50)):
        shift = 350 if row % 2 else 300
        for x in range(shift, 600, 100):
            sd.rectangle(left_bottom=sd.get_point(x, y), right_top=sd.get_point(x + 100, y + 50), width=1)

    start_left_point = sd.get_point(300, 0)
    end_left_point = sd.get_point(300, 250)
    sd.line(start_left_point, end_left_point, width=5)

    start_r_point = sd.get_point(650, 0)
    end_r_point = sd.get_point(650, 250)
    sd.line(start_r_point, end_r_point, width=5)

    start_point_kr = sd.get_point(250, 250)
    point_right_kr = sd.get_point(700, 250)
    konek_kr = sd.get_point(480, 350)
    point_list = [start_point_kr, point_right_kr, konek_kr]
    sd.lines(point_list, closed=True, color=sd.COLOR_RED, width=1)


def draw_homme():
    x, y, = 100, 0
    homme(x, y)

if __name__ == '__main__':
    draw_homme()
    sd.pause()
