# -*- coding: utf-8 -*-
procent = 1.03
educational_grant = 10000
expenses = 12000
expenses_one_month = 12000

total_months = 10
months_with_interest = 9

for _ in range(months_with_interest):
    expenses = expenses * procent
    expenses = expenses + expenses_one_month
    need_money = expenses - educational_grant * total_months
print('Студенту надо попросить', int(need_money), 'рублей')

# зачет!
