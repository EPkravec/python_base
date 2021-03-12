import random

number_comp = 0
number_use = 0
num = 0
win = 'Вы выграли'


def generate_number():
    while True:
        number_comp_str = random.sample(range(10), 4)
        if len(set(number_comp_str)) == 4:
            global number_comp
            number_comp = str((''.join(map(str, number_comp_str))))
            # print(f' Сгенерированное число = {number_comp}')
            return number_comp
        else:
            continue


# def number_user():
#     while True:
#         global num
#         num += 1
#         print(f' Номер попытки {num}')
#         number_us = str(input(' Введите четырехзначное число:  '))
#         global number_use
#         number_use = number_us
#         return number_use, num


def valid():
    global number_comp, number_use

    number_use = list(number_use)
    number_comp = list(number_comp)

    while True:
        if len(number_use) == 4:
            if len(set(number_use)) == len(set(number_comp)):
                return True
            else:
                number_user()

        else:
            number_user()


def process():
    global number_comp, number_use

    number_use = list(number_use)
    number_comp = list(number_comp)

    while True:
        if valid() == True:

            bulls = 0
            cows = 0

            for i in range(4):
                if number_use[i] == number_comp[i]:
                    bulls += 1
                    number_use[i] = ''
                if bulls == 4:
                    return True

            for i in number_comp:
                for j in number_use:
                    if i == j:
                        cows += 1
                        break
            number_user()

    return bulls, cows


if __name__ == '__main__':
    generate_number()
    # number_user()
    valid()
    process()
