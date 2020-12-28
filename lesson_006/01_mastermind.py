# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

# TODO пока делаю все в одном файле после все раскидаю

import random

# todo  проверка на повторяемость цыфр вроде работает а вроде нет (не попадались повторения) + сократь до цикла ?
#
while True:
    number = str(random.randint(1000, 9999))
    random_number_pk = list(number)
    if random_number_pk[0] == random_number_pk[1]:
        random_number_pk[0] = str(random.randint(1, 9))

    if random_number_pk[2] == random_number_pk[1]:
        random_number_pk[2] = str(random.randint(1, 9))

    if random_number_pk[2] == random_number_pk[0]:
        random_number_pk[2] = str(random.randint(1, 9))

    if random_number_pk[3] == random_number_pk[2]:
        random_number_pk[3] = str(random.randint(1, 9))

    if random_number_pk[3] == random_number_pk[1]:
        random_number_pk[3] = str(random.randint(1, 9))

    if random_number_pk[3] == random_number_pk[0]:
        random_number_pk[3] = str(random.randint(1, 9))

    break
print(*random_number_pk, sep="")

# todo  сократить код и сделать как то цикл ?:).  после повторного ввода одного и тогоже цисла на второй раз уходит в брейк
#  если убрать брейк то цикл бесконечный ) как остановить ?:)
number_user = str(input('Введите четырехзначное число c неповторяющимися цифрами - '))
number_user_list = list(number_user)
while True:
    # TODO тут намного проще можно, используй приведение к set-у, чтобы понять, что цифры не повторяются.
    if number_user_list[0] == number_user_list[1]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[0] == number_user_list[2]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[0] == number_user_list[3]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[1] == number_user_list[0]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[1] == number_user_list[2]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[1] == number_user_list[3]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[2] == number_user_list[0]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[2] == number_user_list[1]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[2] == number_user_list[3]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[3] == number_user_list[0]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[3] == number_user_list[1]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)

    if number_user_list[3] == number_user_list[2]:
        number_user = str(input('Вы ввели четырехзначное число c повторяющимися цифрами, введите повторно --'))
        number_user_list = list(number_user)
    break
print('Вы ввели - ', *number_user_list, sep="")


# todo  это процеес сравнения в ""  процесс )
while True:
    dict_otvet = {}
    if number_user_list[0] == random_number_pk[0]:
        apdict_otvet['bulls'] = 1
    else:
        dict_otvet['cows'] = 1
    if number_user_list[1] == random_number_pk[1]:
        dict_otvet['bulls'] = 1
    else:
        dict_otvet['cows'] = 1
    if number_user_list[2] == random_number_pk[2]:
        dict_otvet['bulls'] = 1
    else:
        dict_otvet['cows'] = 1
    if number_user_list[3] == random_number_pk[3]:
        dict_otvet['bulls'] = 1
    else:
        dict_otvet['cows'] = 1
    break
    print(dict_otvet)