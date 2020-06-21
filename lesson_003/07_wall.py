# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

start_left_point_x, start_left_point_y = x, y, = 0, 0
end_right_point_x, end_right_point_y = x1, y1 = 100, 50

# есть мысль: когда программа определяет что координата х == 0 то рисуеться прямоугольник со смещением.
# но почему то стоиться лесенка :(, и чет кривая :), не могу понять в чем ошибка, прошу написать для примера
# надо ли функцию делать тут ????

for x in range(12):
    x += 50
    # TODO как-то слишком запутанно, реализуй сначала простую кладку, без сдвигов,
    #  как решетку, дальше подскажу, как сделать сдвиг.
    if (x / 50) % 2 == 0:
        x = x - 50
        x1 = x1 - 50
        left_point = sd.get_point(x, y)
        right_point = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
    else:
        for x in range(0, 700, 100):
            for y in range(0, 700, 50):
                x += 100
                y += 50
                x1 += 100
                y1 += 50
                left_point = sd.get_point(x, y)
                right_point = sd.get_point(x1, y1)
                sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)
sd.pause()
