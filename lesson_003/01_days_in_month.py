# -*- coding: utf-8 -*-


user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

box_month_28 = (2,)
box_month_30 = (4, 6, 9, 11)
box_month_31 = (1, 3, 5, 7, 8, 10, 12)
# TODO тут надо делать такие проверки, и их будет только 3 if month in box_month_28: ... и ещё 2 проверки для 30 и 31 дней.
if month == box_month_28[0]:
    print('В феврале 28 дней')
elif month == box_month_31[0]:
    print('В январе 31 день')
elif month == box_month_31[1]:
    print('В марте 31 день')
elif month == box_month_31[2]:
    print('В мае 31 день')
elif month == box_month_31[3]:
    print('В июле 31 день')
elif month == box_month_31[4]:
    print('В августе 31 день')
elif month == box_month_31[5]:
    print('В октябре 31 день')
elif month == box_month_31[6]:
    print('В декабре 31 день')
elif month == box_month_30[0]:
    print('В апреле 30 дней')
elif month == box_month_30[1]:
    print('В июне 30 дней')
elif month == box_month_30[2]:
    print('В сентябре 30 дней')
elif month == box_month_30[3]:
    print('В ноябре 30 дней')
else:
    print('Вы не правильно ввели номер месяца')
