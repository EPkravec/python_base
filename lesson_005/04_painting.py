# TODO лучше импортировать не модули, а что-то конкретное внутри них, например в твоем случае ф-ии
from painting import main_rainbow, main_snowfall, main_tree, main_smile, main_the_sun, main_homme
import simple_draw as sd


sd.resolution = (1300, 600)
sd.caption = 'Утро в деревне'

angle = 90
length = 50
angle_1 = 90
length_1 = 30
x, y = 850, 0
x_1, y_1 = 1000, 20


main_rainbow.rab()
main_homme.run_homme()
main_the_sun.sun()
main_smile.run_smail()
main_tree.run_tree(angle, length, x, y)
main_tree.run_tree(angle_1, length_1, x_1, y_1)
main_snowfall.sno()


