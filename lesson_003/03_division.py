# -*- coding: utf-8 -*-

a, b = 179, 37
number_of_repetitions = 0
while number_of_repetitions in range(a):
    number_of_repetitions += 1
    if a == b * number_of_repetitions + 31:
        break
print('Целочисленное деление', a, 'на', b, 'дает', number_of_repetitions)

# todo  я не пойму чего Вам надо, ранее обращаливнимание на это а сейчас что то не понравилось !.
# todo  если программа работает правильно прошу, писать об щибке стилистика или непонятно, допиши коменты  а то я
# todo  а я уже не знаю что тут браться