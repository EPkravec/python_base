# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Радуга дуга 1 и 2 варианты'


x, y = 50, 50
x1, y1 = 350, 450

start_point = sd.get_point(x, y)
end_point = sd.get_point(x1, y1)
sd.line(start_point=start_point, end_point=end_point, width=4)
for x in range(50, 70, 5):
    color = sd.random_color()
    x += 5
    start_point = sd.get_point(x, 50)
    for x1 in range(350, 370, 5):
        x1 += 5
        end_point = sd.get_point(x1, 450)
        sd.line(start_point=start_point, end_point=end_point, width=4)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
