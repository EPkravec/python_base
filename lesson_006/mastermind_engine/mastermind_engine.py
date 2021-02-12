import random
from 01_mastermind import number_us  #Todo что за ???????????????????????


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
                number_us = str(input(':'))
                print(number_comp)
                if number_us == 'check':
                    print(number_comp)
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

if __name__ == '__main__':
    process()

