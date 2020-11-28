# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)


def figur(start_point, angle, length, delta):
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v1.draw()
    if delta < 73:
        end_range = 181
    elif delta > 73:
    end_range = 91
    for next_angle in range(0, end_range, delta):
        next_point = v1.end_point
        next_angle += angle + delta
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw()
    sd.line(start_point=v1.end_point, end_point=start_point)


def triangle(point, angle, length, delta_triangle):
    figur(start_point=point, angle=angle, length=length, delta=delta_triangle)


def square(point, angle, length, delta_square):
    figur(start_point=point, angle=angle, length=length, delta=delta_square)


def pentagon(point, angle, length, delta_pentagon):
    figur(start_point=point, angle=angle, length=length, delta=delta_pentagon)


def hexagon(point, angle, length, delta_hexagon):
    figur(start_point=point, angle=angle, length=length, delta=delta_hexagon)


angle = 30
length = 100

point_triangle = sd.get_point(100, 50)
point_square = sd.get_point(400, 50)
point_pentagon = sd.get_point(400, 400)
point_hexagon = sd.get_point(100, 400)

delta_triangle = 120
delta_square = 90
delta_pentagon = 72
delta_hexagon = 60

triangle(point=point_triangle, angle=angle, length=length, delta_triangle=delta_triangle)
square(point=point_square, angle=angle, length=length, delta_square=delta_square)
pentagon(point=point_pentagon, angle=angle, length=length, delta_pentagon=delta_pentagon)
hexagon(point=point_hexagon, angle=angle, length=length, delta_hexagon=delta_hexagon)
sd.pause()

# зачет!
