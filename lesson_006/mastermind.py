from mastermind_engine import numberComp, process # todo я их только импортирую не вызываю отдельно ??????
print(' Ну что же сыграем в игру ')
print(' ------------------------ ')
print(' Введите четырех значное число')


def numberUser():
    num = 0
    while True:
        num += 1
        print(f'номер попытки {num}')
        number_us = str(input(':'))
        numb = set(number_us)
        if len(numb) != 4:
            print('Должно быть 4 цифры введите повторно')
            continue
        if len(numb) == 4:
            return number_us
        else:
            print('Вы ввели одинаковые цифры')
            continue


number_us = numberUser()

