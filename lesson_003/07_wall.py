# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

x, y, = 0, 0
x1, y1 = 100, 50
for x in range(-101, 700, 100):
    x += 100
    x1 += 100
    for y in range(-51, 700, 50):
        y += 50
        y1 += 50
        left_point = sd.get_point(x, y)
        right_point = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=left_point, right_top=right_point, width=2)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
