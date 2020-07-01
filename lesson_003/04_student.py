# -*- coding: utf-8 -*-


procent = 0.03
educational_grant, expenses = 10000, 12000
month_no_procent = 1
months_with_interest = 9
months_school = 10

annual_educational_grant = educational_grant * months_school
# TODO почему у тебя переменная, которая итерируется - percentage_of_expenses?
#  Это же должен быть счетчик. Тебе в каждой итериции надо наращивать expenses на * 1.03 и
#  от этого числа отнимать степендию, и результат наращивать в need_money уже.
#  Попробуй, если не получится, я подскажу кодом.
for percentage_of_expenses in range(10):
    percentage_of_expenses += (expenses + expenses * procent) * months_with_interest
    percentage_of_expenses_total = expenses + percentage_of_expenses
    need_money = percentage_of_expenses_total - annual_educational_grant


print('Студенту надо попросить', int(need_money), 'рублей')


