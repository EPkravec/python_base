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


def smail(coordinat_face, coordinat_okko_left, coordinat_okko_right, my_list_right_cheek, my_list_left_cheek,
          my_list_center_cheek):

# todo дальше пока не пойму, что нужно сделать и как цикл будет производить привязку всех частей смайла, или как
#  их сгруппировать в один смайл, что бы можно было циклить его, а не его составные части.
sd.pause()
