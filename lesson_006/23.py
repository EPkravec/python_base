vowels = 0
consonants = 0

vowels_box = ['а', 'е', 'ё', 'о', 'и', 'у', 'ы', 'э', 'ю', 'я']
liter_box = 'ь'

line = int(input('Сколько будет строк?'))
i = 0

while i < line:
    text = input()
    for liter in text:
        if liter.isalpha():
            if liter == liter_box:
                vowels += 0
            elif liter in vowels_box:
                vowels += 1

            else:
                consonants += 1
    i += 1

print(f'\n Количество гласных:{vowels} \n Количество согласных:{consonants}')
