import simple_draw as sd


def rab():
    x, y = 640, -250
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

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
    return


rab()

sd.pause()
