import random


def numberComp():
    while True:
        number_comp = [random.randint(0, 9) for _ in range(4)]
        number = set(number_comp)
        if len(number) == 4:
            print(f' из нумберкомп {number_comp}')
            return number_comp

number_comp = numberComp()
number_us =  # todo  а дальше ???? если буду импортировать то буду циклить !!!!!!!

def process():
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


if __name__ == '__main__':
    process()
    numberComp()
# TODO прочитай ещё раз условие, тут должны быть... приведу цитату
#  "Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
#  В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
#  Загаданное число хранить в глобальной переменной.
#  Обратите внимание, что строки - это список символов."
#
