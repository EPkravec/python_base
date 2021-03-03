import random

number_comp = []
number_us = []


def genereatNumber():
    global number_comp
    while True:
        number_comp = [random.randint(0, 9) for _ in range(4)]
        numb_comp_set = set(number_comp)
        if len(numb_comp_set) == 4:
            print(f' Сгенерированное число = {number_comp}')
            return list(number_comp)


def numberUser():
    global number_us
    num = 0
    while True:
        num += 1
        print(f'номер попытки {num}')
        number_us = input(':')
        numb = set(number_us)
        if len(numb) != 4:
            print('Должно быть 4 цифры введите повторно')
            continue
        if len(numb) == 4:
            number_us = list(number_us)
            return number_us
        else:
            print('Вы ввели одинаковые цифры')
            continue

nu = list(number_us)
nc = list(number_comp)



genereatNumber()
numberUser()
print('number_comp', number_comp, type(number_comp))
print('number_comp items',type(number_comp[0]))
print('number_us>', number_us, type(number_us))
print('number_us items >', type(number_us[0]))

print('NEW NC items >', type(nc[0]))
print('NEW NU items ',type(nu[0]))


# while True:
#     nu = number_us
#     nc = number_comp
#
#     bulls = 0
#     for j in range(4):
#         if nu[j] == nc[j]:
#             bulls += 1
#             nu[j] = ''
#             nc[j] = '*'
#
#     if bulls == 4:
#         print('Вы выграли !')
#         break
#
#     cows = 0
#     for j in range(4):
#         entered_digit = nc[j]
#         for i in range(4):
#             if entered_digit == nc[i]:
#                 cows += 1
#                 nc[i] = '*'
#                 break
#     print(f' быков {bulls}')
#     print(f' коров {cows}')
