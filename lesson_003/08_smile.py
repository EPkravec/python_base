# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (700, 700)
sd.background_color = (0, 0, 255)
sd.caption = 'Смайлики'

coordinat_face = sd.get_point(350, 350)
radius_face = 40
sd.circle(center_position=coordinat_face, radius=radius_face)

coordinat_okko_left = sd.get_point(335, 360)
radius__okko_left = 5
sd.circle(center_position=coordinat_okko_left, radius=radius__okko_left)

coordinat_okko_right = sd.get_point(365, 360)
radius__okko_right = 5
sd.circle(center_position=coordinat_okko_right, radius=radius__okko_right)

my_list = [335, 330]
# TODO my_list - должен быть список точек, points
# todo  не могу понять каким образом записываються коокдинаты для lines в списке
sd.lines(point_list=my_list)

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
# TODO здесь ваш код

sd.pause()
