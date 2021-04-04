# -*- coding: utf-8 -*-
#
# class Water:
#
#     def __init__(self):
#         self.name = 'Вода'
#
#     def __add__(self, other):
#         if other == 'Воздух':
#             return self.name + other
#         elif other == 'Огонь':
#             return self.name + other
#         elif other == 'Земля':
#             return self.name + other
#         else:
#             return None
#
#     def __str__(self):
#         return self.name
#
# TODO вот этот класс верно сделан, только не надо переопределять __init__, просто в методе __str__ возвращай 'Воздух'
# class Air:
#
#     def __init__(self):
#         self.name = 'Воздух'
#
#     def __add__(self, other):
#         if other == 'Огонь':
#             return self.name + other
#         elif other == 'Земля':
#             return self.name + other
#         else:
#             return None
#
#     def __str__(self):
#         return self.name
#
#
# class Fire:
#
#     def __init__(self):
#         self.name = 'Огонь'
#
#     def __add__(self, other):
#         if other == 'Земля':
#             return self.name + other
#         else:
#             return None
#
#     def __str__(self):
#         return self.name
#
#
# class Land:
#
#     def __init__(self):
#         self.name = 'Земля'
#
#     def __str__(self):
#         return self.name
#
#
# class Storm:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         return self.name + other
#
#
# class Steam:
#
#     def __init__(self, value):
#         self.name = value
#
#     def __str__(self):
#         return self.name
#
#
# class Mud:
#
#     def __init__(self, value):
#         self.name = value
#
#     def __str__(self):
#         return self.name
#
#
# class Lightning:
#
#     def __init__(self, value):
#         self.name = value
#
#     def __str__(self):
#         return self.name
#
#
# class Dust:
#
#     def __init__(self, value):
#         self.name = value
#
#     def __str__(self):
#         return self.name
#
#
# class Lava:
#
#     def __init__(self, value):
#         self.name = value
#
#     def __str__(self):
#         return self.name
class Elements:

    def __init__(self, name='ящике'):
        self.name = name
        self.water = 'Вода'
        self.air = 'Воздух'
        self.fire = 'Огонь'
        self.land = 'Земля'

    def __str__(self):
        return f'В вашем {self.name} лежат: {self.water}, {self.air}, {self.fire}, {self.land}'

    def create(self, f1, f2):
        if f1 + f2 == 'ВодаВоздух':
            res = 'Шторм'
            return res
        elif f1 + f2 == 'ВодаОгонь':
            res = 'Пар'
            return res
        elif f1 + f2 == 'ВодаЗемля':
            res = 'Грязь'
            return res
        elif f1 + f2 == 'ВоздухОгонь':
            res = 'Молния'
            return res
        elif f1 + f2 == 'ВоздухЗемля':
            res = 'Пыль'
            return res
        elif f1 + f2 == 'ОгоньЗемля':
            res = 'Лава'
            return res
        else:
            return None


s = Elements()
print(f'===========================================================')
print(f'{s}')
print(f'===========================================================')
print(s.water, '+', s.air, '=', s.create(s.water, s.air))
print(s.water, '+', s.fire, '=', s.create(s.water, s.fire))
print(s.water, '+', s.land, '=', s.create(s.water, s.land))

print(s.air, '+', s.fire, '=', s.create(s.air, s.fire))
print(s.air, '+', s.land, '=', s.create(s.air, s.land))
print(s.fire, '+', s.land, '=', s.create(s.fire, s.land))

print(s.land, '+', s.fire, '=', s.create(s.land, s.fire))


# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
# Вода + Воздух = Шторм
# Вода + Огонь = Пар
# Вода + Земля = Грязь
# Воздух + Огонь = Молния
# Воздух + Земля = Пыль
# Огонь + Земля = Лава

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
