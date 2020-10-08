# -*- coding: utf-8 -*-
import simple_draw as sd
import random

sd.resolution = (600, 600)


def figur(point, angle, length):
    triangle(point=point_triangle, angle=angle, length=length)
    square(point=point_square, angle=angle, length=length)
    pentagon(point=point_pentagon, angle=angle, length=length)
    hexagon(point=point_hexagon, angle=angle, length=length)


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
x = random.randint(0, 20)
y = random.randint(0, 20)
point_0 = sd.get_point(x, y)
point_triangle = sd.get_point(x + 100, y + 50)
point_square = sd.get_point(x + 400, y + 50)
point_pentagon = sd.get_point(x + 400, y + 400)
point_hexagon = sd.get_point(x + 100, y + 400)

dict_menu = {
    0: {'red': sd.COLOR_RED},
    1: {'orange': sd.COLOR_ORANGE},
    2: {'yellow': sd.COLOR_YELLOW},
    3: {'green': sd.COLOR_GREEN},
    4: {'cyan': sd.COLOR_CYAN},
    5: {'blue': sd.COLOR_BLUE},
    6: {'purple': sd.COLOR_PURPLE}
}

for key, it in dict_menu.items():
    print(key, ':', *it)

user_data = int(input('Введите желаемый цвет > '))

for number, color_menu in dict_menu.items():
    for color_menu_color, color in color_menu.items():
        while user_data > 6 or user_data < 0:
            print('Вы ввели не корректный номер')
            user_data = int(input('Введите желаемый цвет > '))
            break
        if user_data == number:
            color = color_menu[color_menu_color]
        break


figur(point=point_0, angle=angle, length=length)

sd.pause()
