# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

# educational_grant, expenses = 10000, 12000
# expenses_1 = expenses + expenses * 0.03
# expenses_2 = expenses + expenses_1 * 0.03
# expenses_3 = expenses + expenses_2 * 0.03
# expenses_4 = expenses + expenses_3 * 0.03
# expenses_5 = expenses + expenses_4 * 0.03
# expenses_6 = expenses + expenses_5 * 0.03
# expenses_7 = expenses + expenses_6 * 0.03
# expenses_8 = expenses + expenses_7 * 0.03
# expenses_9 = expenses + expenses_8 * 0.03
# total_expenses = expenses + expenses_1 + expenses_2 + expenses_3 + expenses_4 + expenses_5 + expenses_6 + expenses_7 + expenses_8 + expenses_9
# total_education = educational_grant * 10
# money = total_expenses - total_education
# print('1 вариант для понимания процесса')
# print('Студенту надо попросить', int(money), 'рублей')
#
# procent = 0.03
# monht = 0
# for monht in range(10):
#     monht += 1
#     total_money_monht = expenses + educational_grant + procent * expenses
#     rasxod = expenses - educational_grant
#     money_1 = monht * rasxod + rasxod * procent
#     print('Студенту надо попросить', money_1, 'рублей')


procent = 0.03
educational_grant, expenses = 10000, 12000
rasxodu = expenses - educational_grant
monht = 1
for monht in range(9):
    monht += 1
    if monht == 1:
        continue
    if monht == 2:
        continue
    if monht == 3:
        continue
    if monht == 4:
        continue
    if monht == 5:
        continue
    if monht == 6:
        continue
    if monht == 7:
        continue
    if monht == 8:
        continue
    need_money_mam = monht * (rasxodu + (rasxodu * 9) * procent)
    print('Студенту надо попросить', need_money_mam, 'рублей')