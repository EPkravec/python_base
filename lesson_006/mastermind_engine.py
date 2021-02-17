import random


def genereatNumber():
    number = set([random.randint(0, 9) for _ in range(4)])
    return number


def numberComp(number):
    while True:
        if len(number) == 4:
            print(f' из нумберкомп {number}')
            return number


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


def bulls_cows(number_us, number_comp):
    while True:

        nu = list(number_us)
        nc = list(number_comp)

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


number = genereatNumber()
number_comp = numberComp(number)
number_us = numberUser()
bulls_cows(number_us, number_comp)


# TODO я писал вроде в прошлый раз, чтобы ты тут реализовал отдельные маленькие ф-ии:
#  генерация числа, она есть, это хорошо, можно даже сделать, чтобы эта ф-ия в глобальную переменную закидывала
#  загаданное число. Далее сдделай ф-ию, которая будет принимать число, брать эту глобальную переменную
#  и возвращать коров и быков. Ну и можно сделать ф-ию валидации, котораяя будет принимать число и возвращать,
#  все ли в нем норм, может возвращать true/false. Вот, когда реализуешь все эти ф-ии тут, потом будешь
#  их дергать из главного модуля и никаких конфликтов не будет.
