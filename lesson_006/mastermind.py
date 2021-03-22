from mastermind_engine import generate_number, valid, process

print(' Ну что же сыграем в игру ')
print(' ------------------------------- ')
print(' Введите четырех значное число')
print(' ------------------------------- ')

generate_number()

while True:
    number = input(" Введите число")
    if not valid(number):
        print("Число не валидно, введите заново")
        continue
    bulls, cows = process(number)
    if bulls == 4:
        print("Поздравляю, вы отгадали")
        break
    else:
        print(f" Быков - {bulls} \n "
              f"Коров  - {cows}")
