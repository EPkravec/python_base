# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (600, 600)
color_selection = ['0 : треугольник', '1 : квадрат', '2 : пятиугольник', '3 : шестиугольник']

print('Возможные цвета:', sep='\n', *color_selection)
user_data = int(input('Введите желаемый цвет > '))
if user_data == 0:
    delta = 120
elif user_data == 1:
    delta = 90
elif user_data == 2:
    delta = 72
elif user_data == 3:
    delta = 60
else:
    print('Вы ввели не корректный номер')


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

figur(point=point, angle=angle, length=length)

sd.pause()
