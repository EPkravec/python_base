# -*- coding: utf-8 -*-

a, b = 179, 37
number_of_repetitions = 0
while number_of_repetitions in range(a):
    number_of_repetitions += 1
    # TODO странное условие, распечатку сделай после цикла.
    #  А это условие вообще сделай для выхода из цикла, только без 31, типа пока меньше, то цикл идет.
    if a == b * number_of_repetitions + 31:
        print('Целочисленное деление', a, 'на', b, 'дает', number_of_repetitions)

