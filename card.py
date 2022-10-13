a = int(input('Введите начальный баланс:'))
c = 0
while True:
    b = int(input('Введите стоимость покупки:'))
    if (a - b) >= 0:
        a = a - b
        c = c + 1
    else:
        break
print(f'Сделано покупок: {c}, Остаток на карте: {a}')
