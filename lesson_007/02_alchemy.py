# -*- coding: utf-8 -*-

class Water:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Air:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Fire:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Land:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Storm:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Steam:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Mud:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Lightning:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Dust:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


class Lava:

    def __init__(self, value):
        self.name = value

    def __str__(self):
        return self.name


water = Water(value='Вода')
air = Air(value='Воздух')
fire = Fire(value='Огонь')
land = Land(value='Земля')

print(f'{water} + {air} = {water + air}')
print(f'{water} + {fire} = {water + fire}')
print(f'{water} + {land} = {water + land}')
print(f'{air} + {fire} = {air + air}')
print(f'{air} + {land} = {air + air}')
print(f'{fire} + {land} = {fire + air}')

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
