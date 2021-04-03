# -*- coding: utf-8 -*-

class Water:

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if other == 'Воздух':
            return self.name + other
        elif other == 'Огонь':
            return self.name + other
        elif other == 'Земля':
            return self.name + other
        else:
            return None

    def __str__(self):
        return self.name


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if other == 'Огонь':
            return self.name + other
        elif other == 'Земля':
            return self.name + other
        else:
            return None

    def __str__(self):
        return self.name


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if other == 'Земля':
            return self.name + other
        else:
            return None

    def __str__(self):
        return self.name


class Land:

    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return self.name


class Storm:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other


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


# water = Water(value='Вода')
# air = Air(value='Воздух')
# fire = Fire(value='Огонь')
# land = Land(value='Земля')

print(f'{Water()} + {Air()} = {Water() + Air()}')
print(f'{Water()} + {Fire()} = {Water() + Fire()}')
print(f'{Water()} + {Land()} = {Water() + Land()}')
print(f'{Air()} + {Fire()} = {Air() + Fire()}')
print(f'{Air()} + {Land()} = {Air() + Land()}')
print(f'{Fire()} + {Land()} = {Fire() + Land()}')

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
