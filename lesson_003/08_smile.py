# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (700, 700)
sd.background_color = (0, 0, 255)
sd.caption = 'Смайлики'

def smail(x, y):
    radius_face = 40
    coordinat_face = sd.get_point(x, y)
    radius__okko_left = 5
    radius__okko_right = 5
    coordinat_okko_left = sd.get_point(x - 15, y + 10)
    coordinat_okko_right = sd.get_point(x + 15, y + 10)
    my_list_right_cheek = [sd.get_point(x + 25, y - 10), sd.get_point(x + 10, y - 20)]
    my_list_left_cheek = [sd.get_point(x - 25, y - 10), sd.get_point(x - 10, y - 20)]
    my_list_center_cheek = [sd.get_point(x + 10, y - 20), sd.get_point(x - 10, y - 20)]
    for _ in range(1):
        sd.circle(center_position=coordinat_face, radius=radius_face)
        sd.circle(center_position=coordinat_okko_left, radius=radius__okko_left)
        sd.circle(center_position=coordinat_okko_right, radius=radius__okko_right)
        sd.lines(point_list=my_list_right_cheek)
        sd.lines(point_list=my_list_left_cheek)
        sd.lines(point_list=my_list_center_cheek)


for _ in range(10):
    x = sd.random_number(100, 500)
    y = sd.random_number(100, 500)
    smail(x=x, y=y)

sd.pause()

# зачет!
