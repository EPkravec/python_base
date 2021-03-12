from mastermind_engine import generate_number, valid, process, generate_number, num

print(' Ну что же сыграем в игру ')
print(' ------------------------ ')
print(' Введите четырех значное число')
print(' ------------------------ ')


def number_user():
    while True:
        global num
        num += 1
        print(f' Номер попытки {num}')
        number_us = str(input(' Введите четырехзначное число:  '))
        global number_use
        number_use = number_us
        return number_use


generate_number()
number_user()
valid()
if valid() == True:
    print('Вы выграли')
process()
if process() == True:
    print('Вы выграли')
else:
    print(f'Быков {bulls}')
    print(f'Коров {cows}')
