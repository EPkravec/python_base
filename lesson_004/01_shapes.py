# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 700)


def triangle(point, angle, length):
    # TODO вот тут повторяющиеся строки, их лучше сделать в цикле, потом будет проще сделать одну общую ф-ию.
    #  Можешь вторую часть начинать делать сразу.
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length)
    v3.draw()

# TODO все ф-ии должны быть вверху, потом код, который их использует.
point_triangle = sd.get_point(100, 50)
angle_triangle = 30
length_triangle = 100
triangle(point=point_triangle, angle=angle_triangle, length=length_triangle)


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length)
    v4.draw()


point_square = sd.get_point(700, 50)
angle_square = 30
length_square = 100
square(point=point_square, angle=angle_square, length=length_square)


def pentagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length)
    v5.draw()


point_pentagon = sd.get_point(700, 400)
angle_pentagon = 30
length_pentagon = 100
pentagon(point=point_pentagon, angle=angle_pentagon, length=length_pentagon)


def hexagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length)
    v5.draw()
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length)
    v6.draw()


point_hexagon = sd.get_point(100, 400)
angle_hexagon = 30
length_hexagon = 100
hexagon(point=point_hexagon, angle=angle_hexagon, length=length_hexagon)
sd.pause()

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
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
