# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (255, 255, 255)
sd.caption = 'Радуга дуга 1 и 2 варианты'
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

x, y = 50, 50
x1, y1 = 350, 450
step = (5 + 4) * 6 + 1
rang_start = x + step
i = 0
for x in range(50, rang_start, 9):
    x += 9
    x1 += 9
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x1, y1)
    colors = rainbow_colors[i]
    i += 1
    sd.line(start_point=start_point, end_point=end_point, color=colors, width=4)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
