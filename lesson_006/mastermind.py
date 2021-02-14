print(' Ну что же сыграем в игру ')
print(' ------------------------ ')
print(' Введите четырех значное число')


def numberUser():
    num = 0
    while True:
        num += 1
        print(f'номер попытки {num}')
        number_us = set(str(input(':')))

        if len(number_us) > 4 or len(number_us) < 4:
            print('Должно быть 4 цифры введите повторно')
            continue
        if len(number_us) == 4:
            return number_us
        else:
            print('Вы ввели одинаковые цифры')
            continue


numberUser()

