# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (255, 255, 255)
sd.caption = 'Радуга дуга 1 и 2 задание'
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

start_point_x, start_point_y = x, y = 50, 50
end_point_x, end_point_y = x1, y1 = 350, 450
step = (5 + 4) * 6 + 1
rang_start = x + step
stip = 9     # сумма толщины линии и растояния между линиями
i = 0
for x in range(50, rang_start, stip):
    x += stip
    x1 += stip
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x1, y1)
    colors = rainbow_colors[i]
    i += 1
    sd.line(start_point=start_point, end_point=end_point, color=colors, width=4)

sd.sleep(3)

# 2 задание

sd.clear_screen()

x, y = 680, -250
center = sd.get_point(x, y)
radius = 600
steep = 20
width = 20
i = -1
max_range = radius + steep * 7

for radius in range(radius, max_range, steep):
    i += 1
    colors = rainbow_colors[i]
    sd.circle(center_position=center, radius=radius, color=colors, width=width)

sd.pause()
