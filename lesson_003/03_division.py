# -*- coding: utf-8 -*-

a, b = 179, 37
number_of_repetitions = 1
while a > b * number_of_repetitions + b:
    remainder_of_integer_division = a - b * number_of_repetitions
    number_of_repetitions += 1
    if a == b * number_of_repetitions + remainder_of_integer_division:
        break
print('Целочисленное деление', a, 'на', b, 'дает', number_of_repetitions)
