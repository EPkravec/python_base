# -*- coding: utf-8 -*-


user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

box_month_28 = {2: 28}
box_month_30 = {4: 30, 6: 30, 9: 30, 11: 30}
box_month_31 = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31}
if month == 1:
    print('В январе', box_month_31[month], 'день')
elif month == 2:
    print('В феврале', box_month_28[month], 'дней')
elif month == 3:
    print('В марте', box_month_31[month], 'день')
elif month == 4:
    print('В апреле', box_month_30[month], 'дней')
elif month == 5:
    print('В мае', box_month_31[month], 'день')
elif month == 6:
    print('В июнее', box_month_30[month], 'дней')
elif month == 7:
    print('В июле', box_month_31[month], 'день')
elif month == 8:
    print('В августе', box_month_31[month], 'день')
elif month == 9:
    print('В сентябре', box_month_30[month], 'дней')
elif month == 10:
    print('В октябре', box_month_31[month], 'день')
elif month == 11:
    print('В ноябре', box_month_30[month], 'дней')
elif month == 12:
    print('В декабре', box_month_31[month], 'день')
else:
    print('Вы не правильно ввели номер месяца, нужно ввести значение от 1 до 12')
