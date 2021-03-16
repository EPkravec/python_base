from mastermind_engine import generate_number, valid, process, generate_number, num, number_user

print(' Ну что же сыграем в игру ')
print(' ------------------------ ')
print(' Введите четырех значное число')
print(' ------------------------ ')


# def number_user():
#     while True:
#         global num
#         num += 1
#         print(f' Номер попытки {num}')
#         number_us = str(input(' Введите четырехзначное число:  '))
#         global number_use
#         number_use = number_us
#         return number_use

import pdb;pdb.set_trace()
generate_number() # TODO генерируем число, тут все хорошо
# TODO далее просим юзера ввести число, в общем то, что ты делаешь в ф-ии number_user
# то есть просишь пользователя ввести число, затем проверяешь число на валидность valid(number) , затем... ну ок, ты
# решил не делать функцию, которая проверяет то ли это число, тогда можно вызвать ф-ию process(number) и если быков - 4, 
# то говоришь, что пользователь отгадал, иначе говоришь, пользователю, сколько быков, сколько коров.
# И так по кругу.
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
