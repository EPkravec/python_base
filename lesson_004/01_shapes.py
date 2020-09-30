# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)


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
point_triangle = sd.get_point(100, 50)
point_square = sd.get_point(400, 50)
point_pentagon = sd.get_point(400, 400)
point_hexagon = sd.get_point(100, 400)

triangle(point=point_triangle, angle=angle, length=length)
square(point=point_square, angle=angle, length=length)
pentagon(point=point_pentagon, angle=angle, length=length)
hexagon(point=point_hexagon, angle=angle, length=length)

sd.pause()

# todo  попробовал сделать вот такую ф-ю но к сожалению пока не могу выполнить один критерий ( аргумент в ф-и point)
# todo нужно использовать словарь или список точек для подстановки только пока как реализовать не понимаю
# todo
# def figures(angle, length):
#     v3 = sd.get_vector(start_point=point_triangle, angle=angle, length=length)
#     v3.draw()
#     v4 = sd.get_vector(start_point=point_square, angle=angle, length=length)
#     v4.draw()
#     v5 = sd.get_vector(start_point=point_pentagon, angle=angle, length=length)
#     v5.draw()
#     v6 = sd.get_vector(start_point=point_hexagon, angle=angle, length=length)
#     v6.draw()
#     for next_angle in range(0, 181, delta_triangle):
#         next_point = v3.end_point
#         next_angle += angle + delta_triangle
#         v3 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
#         v3.draw()
#     for next_angle in range(0, 181, delta_square):
#         next_point = v4.end_point
#         next_angle += angle + delta_square
#         v4 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
#         v4.draw()
#     for next_angle in range(0, 271, delta_pentagon):
#         next_point = v5.end_point
#         next_angle += angle + delta_pentagon
#         v5 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
#         v5.draw()
#     for next_angle in range(0, 271, delta_hexagon):
#         next_point = v6.end_point
#         next_angle += angle + delta_hexagon
#         v6 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
#         v6.draw()
#
# angle = 30
# length = 100
# delta_triangle = 120
# delta_square = 90
# delta_pentagon = 72
# delta_hexagon = 60
#
# point_triangle = sd.get_point(100, 50)
# point_square = sd.get_point(400, 50)
# point_pentagon = sd.get_point(400, 400)
# point_hexagon = sd.get_point(100, 400)
#
#
# figures(angle=angle, length=length)
#
#
# sd.pause()
