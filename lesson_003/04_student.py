# -*- coding: utf-8 -*-


procent = 0.03
educational_grant, expenses = 10000, 12000
month_no_procent = 1
months_with_interest = 9
months_school = 10

annual_educational_grant = educational_grant * months_school

for months_with_interest in range(10):
    # TODO тебе надо наращивать expenses в каждой итерации.
    percentage_of_expenses = expenses + (expenses + expenses * procent) * months_with_interest
    need_money = percentage_of_expenses - annual_educational_grant


print('Студенту надо попросить', int(need_money), 'рублей')


