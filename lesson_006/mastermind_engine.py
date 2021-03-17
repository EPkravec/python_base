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
            return number_comp



def valid(number):
    while True:
        if len(number_use) == 4:
            if len(set(number_use)) == len(set(number_comp)):
                return True
            else:
                return False



def process(number):
    while True:
            bulls = 0
            cows = 0

            for i in range(4):
                if number[i] == number_comp[i]:
                    bulls += 1
                    number[i] = ''
                if bulls == 4:
                    return True

            for i in number_comp:
                for j in number:
                    if i == j:
                        cows += 1
                        break

    return bulls, cows


if __name__ == '__main__':
    generate_number()
    valid(number)
    process(number)
