import random
from mastermind import numberUser

# TODO эту ф-ию тебе надо импортировать в mastermind
def numberComp():
    while True:
        number_comp = set([random.randint(0, 9) for _ in range(4)]) # TODO тубу же надо число генерировать, лучше его в
                                                                    #  спиок записать, а не в set, а set использовать уже для того, чтобы понять, что в списке 4 разных числа
        if len(number_comp) > 4 or len(number_comp) < 4: # TODO врядли может быть больше 4-х, тут вообще можно сделать одну проверку, если != 4
            continue
        if len(number_comp) == 4:
            print(number_comp)
            return number_comp
# TODO вот вызов этой ф-ии тоже должен быть в модуле mastermind. Давай пока там импортируй эту ф-ию и вызови генерацию числа
print(numberComp())
number_us = numberUser()

number_comp = numberComp()


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

# TODO прочитай ещё раз условие, тут должны быть... приведу цитату
#  "Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
#  В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
#  Загаданное число хранить в глобальной переменной.
#  Обратите внимание, что строки - это список символов."
#
