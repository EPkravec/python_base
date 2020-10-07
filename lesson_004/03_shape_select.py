# -*- coding: utf-8 -*-
import simple_draw as sd


def figur(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    for next_angle in range(0, 271, delta):
        next_point = v1.end_point
        next_angle += angle + delta
        v1 = sd.get_vector(start_point=next_point, angle=next_angle, length=length)
        v1.draw()


angle = 30
length = 100
point = sd.get_point(300, 300)
dict_menu = {
    0: 'треугольник',
    1: 'квадрат',
    2: 'пятиугольник',
    3: 'шестиугольник'
}
dict_menu_figures = {
    'треугольник': 120,
    'квадрат': 90,
    'пятиугольник': 72,
    'шестиугольник': 60
}
for key, it in dict_menu.items():
    print(key, ':', it)

user_data = int(input('Введите желаемую фигуру > '))

for number, figures_menu in dict_menu.items():
    while user_data > 3 or user_data < 0:
        print('Вы ввели не корректный номер')
        user_data = int(input('Введите желаемый цвет > '))
        break
    if user_data == number:
        delta = dict_menu_figures[figures_menu]
        break

figur(point=point, angle=angle, length=length)

sd.pause()
