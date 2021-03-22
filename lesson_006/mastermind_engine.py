import random

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

            return number_comp


def valid(number):
    if len(number) == 4 == len(set(number)):
        return True
    else:
        return False


def process(number):
    bulls = 0
    cows = 0

    for i in range(4):
        if number[i] == number_comp[i]:
            bulls += 1
        if number[i] in number_comp:
            cows += 1
    cows = cows - bulls

    return bulls, cows


if __name__ == '__main__':
    generate_number()
