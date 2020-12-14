import simple_draw as sd


def sun():
    x, y = 450, 450
    sd.resolution = (1200, 600)
    point = sd.get_point(x, y)
    sd.circle(point, radius=60, color=sd.COLOR_YELLOW, width=0)

    start_p = sd.get_point(x, y)
    end_p = sd.get_point(x, y + 90)
    sd.line(start_p, end_p, width=2)

    end_p1 = sd.get_point(x, y - 90)
    sd.line(start_p, end_p1, width=2)

    end_p2 = sd.get_point(x + 70, y + 70)
    sd.line(start_p, end_p2, width=2)

    end_p3 = sd.get_point(x + 90, y)
    sd.line(start_p, end_p3, width=2)

    end_p4 = sd.get_point(x + 70, y - 70)
    sd.line(start_p, end_p4, width=2)

    end_p5 = sd.get_point(x - 70, y - 70)
    sd.line(start_p, end_p5, width=2)

    end_p6 = sd.get_point(x - 90, y)
    sd.line(start_p, end_p6, width=2)

    end_p7 = sd.get_point(x - 70, y + 70)
    sd.line(start_p, end_p7, width=2)

if __name__ == '__main__':
    sd.pause()
