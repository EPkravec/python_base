import random

# TODO я писал вроде в прошлый раз, чтобы ты тут реализовал отдельные маленькие ф-ии:
#  генерация числа, она есть, это хорошо, можно даже сделать, чтобы эта ф-ия в глобальную переменную закидывала
#  загаданное число. Далее сдделай ф-ию, которая будет принимать число, брать эту глобальную переменную
#  и возвращать коров и быков. Ну и можно сделать ф-ию валидации, котораяя будет принимать число и возвращать,
#  все ли в нем норм, может возвращать true/false. Вот, когда реализуешь все эти ф-ии тут, потом будешь
#  их дергать из главного модуля и никаких конфликтов не будет.
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
        # TODO для определения быков и коров, сделай отдельную ф-ию.
        print(f' быков {bulls}')
        print(f' коров {cows}')


if __name__ == '__main__':
    process()
    numberComp()

