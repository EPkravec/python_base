import simple_draw as sd
import random


def draw_branches(point, angle, length):
    sd.resolution = (1200, 600)
    if length < 5:
        return
    color = sd.COLOR_GREEN
    random_angle = random.randint(18, 42)
    if length > 20:
        color = sd.COLOR_DARK_ORANGE
    v0 = sd.get_vector(start_point=point, angle=angle, length=length)
    v0.draw(color=color)
    v1 = sd.get_vector(start_point=v0.end_point, angle=angle + random_angle, length=length)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v0.end_point, angle=angle - random_angle, length=length)
    v2.draw(color=color)
    random_length = random.uniform(0.6, 0.9)
    next_point_v1 = v1.end_point
    next_point_v2 = v2.end_point
    next_length = length * random_length
    draw_branches(point=next_point_v1, angle=angle + random_angle, length=next_length)
    draw_branches(point=next_point_v2, angle=angle - random_angle, length=next_length)


def run_tree(angle, length, x, y):
    root_point = sd.get_point(x, y)
    angle = angle
    length = length
    draw_branches(point=root_point, angle=angle, length=length)


if __name__ == '__04_painting__':
    sd.pause()
