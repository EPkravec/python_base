from mastermind_engine import generate_number, valid, process, generate_number, num
import pdb


print(' Ну что же сыграем в игру ')
print(' ------------------------ ')
print(' Введите четырех значное число')
print(' ------------------------ ')


pdb.set_trace()
generate_number()
number = input("Введите число")


valid(number)
if valid(number) == True:
    print('Вы выграли')
process(number)
while True:
    if bulls == 4:
        print('Вы выграли')
    else:
        print(f'Быков {bulls}')
        print(f'Коров {cows}')
