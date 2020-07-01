# -*- coding: utf-8 -*-


user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

box_month_28 = (2,)
box_month_30 = (4, 6, 9, 11)
box_month_31 = (1, 3, 5, 7, 8, 10, 12)

if month in box_month_28:
    print('В', '28 дней')
elif month in box_month_30:
    print('В', '30 день')
elif month in box_month_31:
    print('В', '31 день')
else:
    print('Вы не правильно ввели номер месяца')

# зачет!
