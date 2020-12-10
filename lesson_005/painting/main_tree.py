import simple_draw as sd
import random

sd.resolution = (900, 800)


def draw_branches(point, angle, length):
    if length < 10:
        return
    random_angle = random.randint(18, 42)
    v0 = sd.get_vector(start_point=point, angle=angle, length=length)
    v0.draw()
    v1 = sd.get_vector(start_point=v0.end_point, angle=angle + random_angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v0.end_point, angle=angle - random_angle, length=length)
    v2.draw()
    random_length = random.uniform(0.6, 0.9)
    next_point_v1 = v1.end_point
    next_point_v2 = v2.end_point
    next_length = length * random_length
    draw_branches(point=next_point_v1, angle=angle + random_angle, length=next_length)
    draw_branches(point=next_point_v2, angle=angle - random_angle, length=next_length)


root_point = sd.get_point(300, 30)
angle = 90
length = 100
draw_branches(point=root_point, angle=angle, length=length)

sd.pause()

