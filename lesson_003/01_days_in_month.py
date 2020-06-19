# -*- coding: utf-8 -*-


user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
box_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
if month == 1:
    print('В январе', box_month[month], 'день')
elif month == 2:
    print('В феврале', box_month[month], 'дней')
elif month == 3:
    print('В феврале', box_month[month], 'день')
elif month == 4:
    print('В феврале', box_month[month], 'дней')
elif month == 5:
    print('В феврале', box_month[month], 'день')
elif month == 6:
    print('В феврале', box_month[month], 'дней')
elif month == 7:
    print('В феврале', box_month[month], 'день')
elif month == 8:
    print('В феврале', box_month[month], 'день')
elif month == 9:
    print('В феврале', box_month[month], 'дней')
elif month == 10:
    print('В феврале', box_month[month], 'день')
elif month == 11:
    print('В феврале', box_month[month], 'дней')
elif month == 12:
    print('В феврале', box_month[month], 'день')
else:
    print('Вы не правильно ввели номер месяца, нужно ввести значение от 1 до 12')
