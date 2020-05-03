#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Отец', 'Мама', 'Сын', 'Жена']

# список списков приблизителного роста членов вашей семьи
# ['имя', рост]
my_family_height = [['Павел', 190],
                    ['Ирина', 170],
                    ['Дмитрий', 130],
                    ['Ольга', 180]]

print('Рост отца -', my_family_height[0][1], 'см')
print('Общий рост моей семьи -',
      my_family_height[0][1]
      + my_family_height[1][1]
      + my_family_height[2][1]
      + my_family_height[3][1], 'см')

#  второй вариант
# да, вынести в отдельную переменную - хорошая идея
my_family_height_all = (my_family_height[0][1]
                        + my_family_height[1][1]
                        + my_family_height[2][1]
                        + my_family_height[3][1])
print('Общий рост моей семьи -', my_family_height_all, 'см')

# молодец
# зачет!
