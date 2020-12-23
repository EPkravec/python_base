from painting.main_rainbow import rab
from painting.main_tree import run_tree
from painting.main_smile import run_smail
from painting.main_the_sun import sun
from painting.main_homme import draw_homme
from painting.main_snowfall import sno
import simple_draw as sd


sd.resolution = (1300, 600)
sd.caption = 'Утро в деревне'

angle = 90
length = 25
angle_1 = 90
length_1 = 30
x, y = 950, 250
x_1, y_1 = 1000, 20


rab()
draw_homme()
sun()
run_smail()
run_tree(angle, length, x, y)
run_tree(angle_1, length_1, x_1, y_1)
sno()


