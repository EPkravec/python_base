import simple_draw as sd


def smail(x, y):
    sd.resolution = (1200, 600)
    radius_face = 40
    coordinat_face = sd.get_point(x, y)
    radius__okko_left = 5
    radius__okko_right = 5
    coordinat_okko_left = sd.get_point(x - 15, y + 10)
    coordinat_okko_right = sd.get_point(x + 15, y + 10)
    my_list_right_cheek = [sd.get_point(x + 25, y - 10), sd.get_point(x + 10, y - 20)]
    my_list_left_cheek = [sd.get_point(x - 25, y - 10), sd.get_point(x - 10, y - 20)]
    my_list_center_cheek = [sd.get_point(x + 10, y - 20), sd.get_point(x - 10, y - 20)]

    sd.circle(center_position=coordinat_face, radius=radius_face)
    sd.circle(center_position=coordinat_okko_left, radius=radius__okko_left)
    sd.circle(center_position=coordinat_okko_right, radius=radius__okko_right)
    sd.lines(point_list=my_list_right_cheek)
    sd.lines(point_list=my_list_left_cheek)
    sd.lines(point_list=my_list_center_cheek)

    start_skelet = sd.get_point(x, y - radius_face)
    end_skelet = sd.get_point(x, y - 150)
    sd.line(start_skelet, end_skelet, width=2)

    start_left_nog = sd.get_point(x, y - 150)
    end_left_nog = sd.get_point(x + 50, y - 200)
    sd.line(start_left_nog, end_left_nog, width=2)

    start_right_nog = sd.get_point(x, y - 150)
    end_right_nog = sd.get_point(x - 50, y - 200)
    sd.line(start_right_nog, end_right_nog, width=2)

    start_ryku = sd.get_point(x - 50, y - 80)
    end_ryku = sd.get_point(x + 50, y - 80)
    sd.line(start_ryku, end_ryku, width=2)


def run_smail():
    x = 650
    y = 200
    smail(x=x, y=y)


if __name__ == '__main__':
    sd.pause()
