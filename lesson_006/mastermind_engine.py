import random
# TODO глобальные переменные надо писать caps lock-ом, чтобы в коде сразу было понятно, что это глобальная переменная.
number_comp = ''
number_use = 0
num = 0
win = 'Вы выграли'


def generate_number():
    while True:
        number_comp_str = random.sample(range(10), 4)
        if len(set(number_comp_str)) == 4:
            global number_comp
            number_comp = str((''.join(map(str, number_comp_str))))
            print(number_comp)
            return number_comp



def valid(number):
    # TODO ты же получил number, это и есть число, которое ввел пользователь, его и надо проверять. И зачем цикл, тут будет зацикливание, если в числе будет не 4 символа.
    # while True:
    #     if len(number_use) == 4:
    #         if len(set(number_use)) == len(set(number_comp)):
    #             return True
    #         else:
    #             return False
    if len(number) == 4 == len(set(number)):
        return True
    else:
        return False


def process(number):
    # TODO тоже не понял, зачем тут цикл
    # while True:
    #         bulls = 0
    #         cows = 0
    #
    #         for i in range(4):
    #             if number[i] == number_comp[i]:
    #                 bulls += 1
    #                 number[i] = ''
    #             if bulls == 4:
    #                 return True # TODO зачем тут это, ф-ия должна в любом случае возвращать коров и быков, зля чего True? То, что быка 4 - надо определять в главном модуле.
    #
    #         for i in number_comp:
    #             for j in number:
    #                 if i == j:
    #                     cows += 1
    #                     break
    #
    # return bulls, cows
    bulls = 0
    cows = 0

    for i in range(4):
        if number[i] == number_comp[i]:
            bulls += 1
        # TODO тут можно объединить в один цикл
        if number[i] in number_comp:
            cows += 1
    cows = cows - bulls # TODO тут удаляем дубликаты в коровах, которые получились, когда на одних и тех же позициях одинаковые цифры.

    return bulls, cows


if __name__ == '__main__':
    generate_number()
