# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1000, 700)
color_selection = ['0 : red', '1 : orange', '2 : yellow', '3 : green', '4 : cyan', '5 : blue', '6 : purple']

print('Возможные цвета:', sep='\n', *color_selection)
user_data = int(input('Введите желаемый цвет > '))
if user_data == 0:
    color = sd.COLOR_RED
elif user_data == 1:
    color = sd.COLOR_ORANGE
elif user_data == 2:
    color = sd.COLOR_YELLOW
elif user_data == 3:
    color = sd.COLOR_GREEN
elif user_data == 4:
    color = sd.COLOR_CYAN
elif user_data == 5:
    color = sd.COLOR_BLUE
elif user_data == 6:
    color = sd.COLOR_PURPLE
else:
    print('Вы ввели не корректный номер')


def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    for next_angle in range(0, 181, delta_triangle):
        next_point = v1.end_point
        next_angle += angle + delta_triangle
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw(color=color)


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    for next_angle in range(0, 181, delta_square):
        next_point = v1.end_point
        next_angle += angle + delta_square
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw(color=color)


def pentagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    for next_angle in range(0, 271, delta_pentagon):
        next_point = v1.end_point
        next_angle += angle + delta_pentagon
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw(color=color)


def hexagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    for next_angle in range(0, 271, delta_hexagon):
        next_point = v1.end_point
        next_angle += angle + delta_hexagon
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw(color=color)


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
