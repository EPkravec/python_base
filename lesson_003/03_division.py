# -*- coding: utf-8 -*-


a, b = 179, 37
i = 0
for i in range(10):
    if a == b * i + 31:
        print('Целочисленное деление', a, 'на', b, 'дает', i)
