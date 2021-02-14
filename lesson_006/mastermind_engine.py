import random
# TODO смотри, mastermind импортировать не надо, я же писал, чтобы не было перекрестных импортов.
#  тут просто напиши ф-ию, которая будет генерировать number_us1, и тут же создай глобальную переменную,
#  которая будет хранить результат, и потом к ней уже будешь обращаться.
from mastermind import number_us1


def process():
    game = True
    while game == True:
        number = [random.randint(0, 9) for _ in range(4)]

        if number[0] != number[1] and number[0] != number[2] and number[0] != number[3] and \
                number[1] != number[2] and number[1] != number[3] and \
                number[2] != number[3]:

            number_comp = str(number[0]) + str(number[1]) + str(number[2]) + str(number[3])

            game = False
            num = 0

            while game == False:
                num += 1
                print(f'номер попытки {num}')
                number_us = number_us1  # todo вот так сделал !
                print(number_comp)
                if number_us == 'check':
                    print(number_comp)
                    continue
                if len(number_us) > 4:
                    # TODO вроде тоже писал, что все взаимодействие с юзером, то есть все принты должны
                    #  быть в главном модуле, то есть в mastermind
                    print('Должно быть 4 цифры введите повторно')
                    continue
                if len(number_us) < 4:
                    print('Должно быть 4 цифры введите повторно')
                    continue
                # TODO я уже писал вроде, что если число у нас будет строкой, и мы преобразуем его в t, то получим на
                #  выходе set, с котором не будет дублей и если длина этого set-а будет 4,
                #  то значит, что все цифры разные.
                if number_us[0] != number_us[1] and number_us[0] != number_us[2] and number_us[0] != number_us[3] and \
                        number_us[1] != number_us[2] and number_us[1] != number_us[3] and \
                        number_us[2] != number_us[3]:
                    print()
                else:
                    print('Вы ввели одинаковые цифры')
                    continue

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
        else:
            continue
    return
# TODO прочитай ещё раз условие, тут должны быть... приведу цитату
#  "Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
#  В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
#  Загаданное число хранить в глобальной переменной.
#  Обратите внимание, что строки - это список символов."

if __name__ == '__main__':
    process()
