# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (600, 600)

# TODO не совсем так), тебе надо сделать базовую ф-ию, выглядеть она будет как triangle, например, а сама triangle внутри будет только одной строкой вызывать юту ф-ию с нужными параметрами, все остальные ф-ии - также)
def figur(point, angle, length):
    triangle(point=point_triangle, angle=angle, length=length)
    square(point=point_square, angle=angle, length=length)
    pentagon(point=point_pentagon, angle=angle, length=length)
    hexagon(point=point_hexagon, angle=angle, length=length)


def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    for next_angle in range(0, 181, delta_triangle):
        next_point = v1.end_point
        next_angle += angle + delta_triangle
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw()


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    for next_angle in range(0, 181, delta_square):
        next_point = v1.end_point
        next_angle += angle + delta_square
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw()


def pentagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    for next_angle in range(0, 271, delta_pentagon):
        next_point = v1.end_point
        next_angle += angle + delta_pentagon
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw()


def hexagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    for next_angle in range(0, 271, delta_hexagon):
        next_point = v1.end_point
        next_angle += angle + delta_hexagon
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw()


angle = 30
length = 100
delta_triangle = 120
delta_square = 90
delta_pentagon = 72
delta_hexagon = 60
x = random.randint(0, 20)
y = random.randint(0, 20)
point_0 = sd.get_point(x, y)
point_triangle = sd.get_point(x + 100, y + 50)
point_square = sd.get_point(x + 400, y + 50)
point_pentagon = sd.get_point(x + 400, y + 400)
point_hexagon = sd.get_point(x + 100, y + 400)

figur(point=point_0, angle=angle, length=length)

sd.pause()
