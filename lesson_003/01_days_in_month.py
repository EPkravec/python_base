# -*- coding: utf-8 -*-


user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

box_month_28 = (2,)
box_month_30 = (4, 6, 9, 11)
box_month_31 = (1, 3, 5, 7, 8, 10, 12)
box_month_name = {1: 'Январе',
                  2: 'Феврале',
                  3: 'Марте',
                  4: 'Апреле',
                  5: 'Мае',
                  6: 'Июне',
                  7: 'Июле',
                  8: 'Августе',
                  9: 'Сентябре',
                  10: 'Октябре',
                  11: 'Ноябре',
                  12: 'Декабре',
                  }
if month in box_month_28:
    print('В', box_month_name[month], '28 дней')
elif month in box_month_30:
    print('В', box_month_name[month], '30 день')
elif month in box_month_31:
    print('В', box_month_name[month], '31 день')
else:
    print('Вы не правильно ввели номер месяца')
