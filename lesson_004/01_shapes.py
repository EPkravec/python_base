# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)


def figur(start_point, angle, length):
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v1.draw()
    for next_angle in range(0, 181, delta):
        next_point = v1.end_point
        next_angle += angle + delta
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw()
    sd.line(start_point=v1.end_point, end_point=start_point)


def triangle(point, angle, length):
    figur(start_point=point, angle=angle, length=length)


def square(point, angle, length):
    figur(start_point=point, angle=angle, length=length)


def pentagon(point, angle, length):
    figur(start_point=point, angle=angle, length=length)


def hexagon(point, angle, length):
    figur(start_point=point, angle=angle, length=length)


angle = 30
length = 100

point_triangle = sd.get_point(100, 50)
point_square = sd.get_point(400, 50)
point_pentagon = sd.get_point(400, 400)
point_hexagon = sd.get_point(100, 400)

delta = delta_triangle = 120
triangle(point=point_triangle, angle=angle, length=length)
delta = delta_square = 90
square(point=point_square, angle=angle, length=length)
delta = delta_pentagon = 72
pentagon(point=point_pentagon, angle=angle, length=length)
delta = delta_hexagon = 60
hexagon(point=point_hexagon, angle=angle, length=length)
sd.pause()
