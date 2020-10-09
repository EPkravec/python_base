# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (600, 600)


def figur(start_point, angle, length):
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v1.draw(color=color)
    if delta < 73:
        end_range = 181
    elif delta > 73:
        end_range = 91
    for next_angle in range(0, end_range, delta):
        next_point = v1.end_point
        next_angle += angle + delta
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw(color=color)
    sd.line(start_point=v1.end_point, end_point=start_point, color=color)


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
# TODO не рекомендуется использовать названия структур данных в именах переменных, тут может быть название цвета
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
        while user_data > 6 or user_data < 0: # TODO у тебя же есть словарь dict_menu, его и используй if user_data not in dict_menu ...
            print('Вы ввели не корректный номер')
            user_data = int(input('Введите желаемый цвет > '))
            break
    if user_data == number:
        color = color_menu[color_menu_color]
        break

delta = delta_triangle = 120
triangle(point=point_triangle, angle=angle, length=length)
delta = delta_square = 90
square(point=point_square, angle=angle, length=length)
delta = delta_pentagon = 72
pentagon(point=point_pentagon, angle=angle, length=length)
delta = delta_hexagon = 60
hexagon(point=point_hexagon, angle=angle, length=length)
sd.pause()
