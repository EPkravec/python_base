# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)
sd.background_color = (0, 0, 255)
sd.caption = 'Стена'

x, y, = 0, 0

# for y in range(0, 700, 50):
#     if (y / 50) % 2 == 1:
#         shift = 0
#     else:
#         shift = 50
#     for x in range(shift, 700, 100):
#         left_point = sd.get_point(x, y)
#         right_point = sd.get_point(x + 100, y + 50)
#         sd.rectangle(left_bottom=left_point, right_top=right_point, width=1)


for row, y in enumerate(range(0, 700, 50)):
    shift = 0 if row % 2 else -50
    for x in range(shift, 700, 100):
        sd.rectangle(left_bottom=sd.get_point(x, y), right_top=sd.get_point(x + 100, y + 50), width=1)
sd.pause()

#зачёт!