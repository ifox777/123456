s = input()
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
vowels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
counter1, counter2 = 0, 0
for i in s:
    if i in consonants:
        counter1 += 1
    if i in vowels:
        counter2 += 1

print('Количество гласных букв равно', counter2)
print('Количество согласных букв равно', counter1)
