# -*- coding: utf-8 -*-

a, b = 179, 37
number_of_repetitions = 0
# TODO не знаю какое условие поставить. Если только меньше А, делает 5 циклов это больше нужного,
#  не пойму пока какое условие поставить или как написаный  правильно аргументировать
while number_of_repetitions * b < a - b:
    remainder_of_integer_division = a - b * number_of_repetitions
    number_of_repetitions += 1
    if a == b * number_of_repetitions + remainder_of_integer_division:
        break
print('Целочисленное деление', a, 'на', b, 'дает', number_of_repetitions)
