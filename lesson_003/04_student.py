# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
# TODO это надо делать в цикле.
expenses_1 = expenses + expenses * 0.03
expenses_2 = expenses + expenses_1 * 0.03
expenses_3 = expenses + expenses_2 * 0.03
expenses_4 = expenses + expenses_3 * 0.03
expenses_5 = expenses + expenses_4 * 0.03
expenses_6 = expenses + expenses_5 * 0.03
expenses_7 = expenses + expenses_6 * 0.03
expenses_8 = expenses + expenses_7 * 0.03
expenses_9 = expenses + expenses_8 * 0.03
total_expenses = expenses + expenses_1 + expenses_2 + expenses_3 + expenses_4 + expenses_5 + expenses_6 + expenses_7 + expenses_8 + expenses_9
total_education = educational_grant * 10
money = total_expenses - total_education
print('1 вариант для понимания процесса')
print('Студенту надо попросить', int(money), 'рублей')

print('2 вариант для цикла')
procent = 0.03
# TODO нейминг, тут наверное счетчик месяцев мог бы быть.
i = 1
while i < 10:
    i += 1
    # TODO не совсем понял, зачем эта проверка...
    if i in range(11):
        #  TODO нет, тебе надо в цикле высчитывать текущую стоимость текущего
        #   мес и из неё вычитать стипендию и все это скидывать в тотал
        rasxod = expenses - educational_grant
        money_1 = int(i * rasxod + rasxod * procent)
        print('Студенту надо попросить', money_1, 'рублей')