import random

# TODO что за название такое ф-ии, все буковки должны быть маленькие и разделитель - нижнее подчеркивание,
#  ты в java стиле пишешь.
def numberComp():
    one_number = random.randint(0, 9)
    two_number = random.randint(0, 9)
    fhree_number = random.randint(0, 9)
    four_number = random.randint(0, 9)
    # TODO сделай проверку проще, можно преобразовать число к set-у и так понять, что все числа внутри разные, ещё пригодится ф-ия len()
    #  И у тебя если число не прошло по этим условиям, то ф-ия возвращает None, а по идее она должна дальше генерировать, пока не получится.
    #  Можно ещё постепенно генерировать число, сначала рандом из всех цифр, потом из всех кроме той, которая уже выпала итд.
    if one_number != two_number and one_number != fhree_number and one_number != four_number and \
            two_number != fhree_number and two_number != four_number and \
            fhree_number != four_number:
        number_comp = str(one_number) + str(two_number) + str(fhree_number) + str(four_number)
        print(type(number_comp))
        return number_comp

# TODO тут тоже название поправь.
def numberUS():
    num = 0
    while True:
        num += 1
        # TODO также все взаимодействие с пользователем должнор проходить через главный модуль программы, тут только набор ф-ий.
        print(f'номер попытки {num}')
        number_us = str(input(':'))
        if number_us == 'check':
            print(numberComp())
            continue
        if len(number_us) > 4:
            print('Должно быть 4 цифры введите повторно')
            continue
        if len(number_us) < 4:
            print('Должно быть 4 цифры введите повторно')
            continue
        if number_us[0] != number_us[1] and number_us[0] != number_us[2] and number_us[0] != number_us[3] and \
                number_us[1] != number_us[2] and number_us[1] != number_us[3] and \
                number_us[2] != number_us[3]:
            print('')
        else:
            print('Вы ввели одинаковые цифры')
            continue

        nu = list(number_us)
        nc = list(numberComp()) # TODO у тебя ф-ия numberComp возвращает None

        bulls = 0
        for j in range(4):
            if nu[j] == nc[j]:
                bulls += 1
                nu[j] = ''
                nc[j] = '*'

        if bulls == 4:
            print('Вы выграли !')
            break

        cows = 0
        for j in range(4):
            entered_digit = nc[j]
            for i in range(4):
                if entered_digit == nc[i]:
                    cows += 1
                    nc[i] = '*'
                    break

        print(f' быков {bulls}')
        print(f' коров {cows}')

    return
