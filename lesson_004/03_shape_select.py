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
# TODO тут тоже объедини эти словари, потом будет проще добавлять новые варианты, если будет требоваться
dict_menu = {
    0: {'треугольник': 120},
    1: {'квадрат': 90},
    2: {'пятиугольник': 72},
    3: {'шестиугольник': 60}
}

for key, it in dict_menu.items():
    print(key, ':', *it)

user_data = int(input('Введите желаемую фигуру > '))

for number, figures_delta in dict_menu.items():
    for figures_delta_key, delta in figures_delta.items():
        while user_data > 3 or user_data < 0:
            print('Вы ввели не корректный номер')
            user_data = int(input('Введите желаемый цвет > '))
            break
        if user_data == number:
            delta = figures_delta[figures_delta_key]
            print(type(delta), delta)
            break

figur(point=point, angle=angle, length=length)

sd.pause()
