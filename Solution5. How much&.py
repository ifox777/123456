n = input()
counter1 = 0
counter2 = 0
for i in n:
    if i == '+':
        counter1 += 1
    if i == '*':
        counter2 += 1
print('Символ + встречается', counter1, 'раз')
print('Символ * встречается', counter2, 'раз')

