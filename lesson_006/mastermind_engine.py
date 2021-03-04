import random

number_comp = []
number_us = []
num = 0
bulls = 0
cows = 0


def genereatNumber():
    global number_comp
    while True:
        number_comp = [random.randint(0, 9) for _ in range(4)]
        numb_comp_set = set(number_comp)
        if len(numb_comp_set) == 4:
            number_comp[0] = str(number_comp[0])
            number_comp[1] = str(number_comp[1])
            number_comp[2] = str(number_comp[2])
            number_comp[3] = str(number_comp[3])
            print(f' Сгенерированное число = {number_comp}')
            return number_comp


def numberUser():
    global number_us, num
    while True:
        num += 1
        print(f'номер попытки {num}')
        number_us = input('Введите число:')
        numb = set(number_us)
        if len(numb) != 4:
            print('Должно быть 4 цифры введите повторно')
            continue
        if len(numb) == 4:
            return number_us
        else:
            print('Вы ввели одинаковые цифры')
            continue


def valid():
    global number_comp, number_us

    if set(number_comp) == set(number_us):
        return True
    else:
        return False


def process():
    global bulls, cows, num

    if valid() == True:
        print('Вы Выграли')
    if valid() == False:

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
                for i in range(4):
                    if nc[j] == nc[i]:
                        cows += 1
                        nc[i] = '*'
                        break

            print(f' быков {bulls}')
            print(f' коров {cows}')

            numberUser()
    return bulls, cows


if __name__ == '__main__':
    genereatNumber()
    numberUser()
    valid()
    process()
