# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)


def triangle(point, angle, length, delta):
    while angle > 360:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_angle_triangle = angle + delta_triangle
    next_point = v1.end_point
    # TODO сделай пожалуйста в цикле, использовать рекурсию, где в этом нет особой необходимости - не надо, как минимум усложняет чтение кода.
    triangle(point=next_point, angle=next_angle_triangle, length=length, delta=delta)


def square(point, angle, length, delta):
    while angle > 360:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_angle_square = angle + delta_square
    next_point = v1.end_point
    square(point=next_point, angle=next_angle_square, length=length, delta=delta)


def pentagon(point, angle, length, delta):
    while angle > 360:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_angle_pentagon = angle + delta_pentagon
    next_point = v1.end_point
    pentagon(point=next_point, angle=next_angle_pentagon, length=length, delta=delta)


def hexagon(point, angle, length, delta):
    while angle > 360:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_angle_hexagon = angle + delta_hexagon
    next_point = v1.end_point
    hexagon(point=next_point, angle=next_angle_hexagon, length=length, delta=delta)


point_triangle = sd.get_point(100, 50)
angle = 30
length = 100
delta_triangle = 120
delta_square = 90
delta_pentagon = 72
delta_hexagon = 60
point_square = sd.get_point(400, 50)
point_pentagon = sd.get_point(400, 400)
point_hexagon = sd.get_point(100, 400)


triangle(point=point_triangle, angle=angle, length=length, delta=delta_triangle)
square(point=point_square, angle=angle, length=length, delta=delta_square)
pentagon(point=point_pentagon, angle=angle, length=length, delta=delta_pentagon)
hexagon(point=point_hexagon, angle=angle, length=length, delta=delta_hexagon)

sd.pause()


# # Часть 2 (делается после зачета первой части)
# #
# # Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# # Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
