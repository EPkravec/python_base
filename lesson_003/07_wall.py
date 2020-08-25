# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

x, y, = 0, 0

for y in range(0, 700, 50):
    if (y / 50) % 2 == 1:
        # TODO Обратите внимание, что и тут, и ниже код с циклом почти одинаковый
        # TODO Давайте попробуем это исправить.
        # TODO Чтобы это сделать, можно сделать один if/else, в котором будет определяться переменная shift
        # TODO например, если условие выполняется, то shift = 0, иначе = 50
        # TODO А уже после if/else запускать один цикл
        # TODO И в идеале использовать shift не внутри создания точек
        # TODO а в диапазоне цикла, т.е. писать не range(0, 700, 100), а range(shift, 700, 100)

        for x in range(0, 700, 100):
            left_point = sd.get_point(x, y)
            right_point = sd.get_point(x + 100, y + 50)
            sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
    if (y / 50) % 2 == 0:
        shift = 50
        for x in range(0, 700, 100):
            left_point = sd.get_point(x + shift, y)
            right_point = sd.get_point(x + 100 + shift, y + 50)
            print(x,y)
            sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
sd.pause()
