# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

x, y, = 0, 0
x1, y1 = 100, 50
x_shift, y_shift, = -50, 50
x1_shift, y1_shift = 50, 100

for y in range(0, 700, 50):
    y += 50
    y1 += 50
    if (y / 50) % 2 == 0:
        x = x_shift
        x1 = x1_shift
    elif (y / 50) % 2 == 1:
        x += 100
        x1 += 100
        for x in range(0, 700, 100):
            print(x, x1)
            left_point = sd.get_point(x, y)
            right_point = sd.get_point(x1, y1)
            sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
sd.pause()

# todo  сделал обычную кладку, отлично, теперь подумай, как сделать сдвиг по х на каждом уровне.
#  Для этого надо ввести переменную сдвиг и на каждой итерации внешнего цикла менять её.
# при проверке пошагового выполнения програмы обнаружил что беруться какието не те координаты для первых точек
# не могу понять почему и кто их ставил)))
