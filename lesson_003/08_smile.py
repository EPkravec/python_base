# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (700, 700)
sd.background_color = (0, 0, 255)
sd.caption = 'Смайлики'

coordinat_face = sd.get_point(350, 350)
radius_face = 40
sd.circle(center_position=coordinat_face, radius=radius_face)

coordinat_okko_left = sd.get_point(335, 360)
radius__okko_left = 5
sd.circle(center_position=coordinat_okko_left, radius=radius__okko_left)

coordinat_okko_right = sd.get_point(365, 360)
radius__okko_right = 5
sd.circle(center_position=coordinat_okko_right, radius=radius__okko_right)

my_list_right_cheek = [sd.get_point(375, 340), sd.get_point(360, 330)]
sd.lines(point_list=my_list_right_cheek)

my_list_left_cheek = [sd.get_point(325, 340), sd.get_point(340, 330)]
sd.lines(point_list=my_list_left_cheek)

my_list_center_cheek = [sd.get_point(360, 330), sd.get_point(340, 330)]
sd.lines(point_list=my_list_center_cheek)

sd.sleep(3)
sd.clear_screen()  # 10 смайликов рандомно


def smail(point):
    radius_face = 40
    coordinat_face = sd.get_point(350, 350)
    coordinat_okko_left = sd.get_point(335, 360)
    radius__okko_left = 5
    coordinat_okko_right = sd.get_point(365, 360)
    radius__okko_right = 5
    my_list_right_cheek = [sd.get_point(375, 340), sd.get_point(360, 330)]
    my_list_left_cheek = [sd.get_point(325, 340), sd.get_point(340, 330)]
    my_list_center_cheek = [sd.get_point(360, 330), sd.get_point(340, 330)]
    for _ in range(10):
        sd.circle(center_position=coordinat_face, radius=radius_face)
        sd.circle(center_position=coordinat_okko_left, radius=radius__okko_left)
        sd.circle(center_position=coordinat_okko_right, radius=radius__okko_right)
        sd.lines(point_list=my_list_right_cheek)
        sd.lines(point_list=my_list_left_cheek)
        sd.lines(point_list=my_list_center_cheek)


for _ in range(10):
    point = sd.random_point()
    smail(point=point)
    sd.circle(center_position=coordinat_face, radius=radius_face)
    sd.circle(center_position=coordinat_okko_left, radius=radius__okko_left)
    sd.circle(center_position=coordinat_okko_right, radius=radius__okko_right)
    sd.lines(point_list=my_list_right_cheek)
    sd.lines(point_list=my_list_left_cheek)
    sd.lines(point_list=my_list_center_cheek)

sd.pause()
# todo  чет не так %) возможно в def smail  нужно еще переменные ? или принципиально нето?