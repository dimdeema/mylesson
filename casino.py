import random
a = random.randint(1, 10)
b = random.randint(1, 2)

i = 0
while i<5:
    i = i + 1 # i += 1
    c = int(input('Введите число от 1 до 10:'))
    d = int(input('Введите число от 1 до 2 (1 красный, 2 - черный):'))
    if a == c and b == d:
        print(f'Вы угадали число и цвет: {c} {d}')
        break
    elif a != c and b == d:
        print(f'Вы не угадали число: {c}, но угадали цвет: {d}')
    elif a == c and b != d:
        print(f'Вы угадали число: {c}, но не угадали цвет: {d}')
    else:
        print(f'Вы не угадали число и цвет: {c} {d}. Попробуйте еще раз')
else:
    print(f'Вы не угадали число и цвет: {c} {d}.Ваши попытки закончились')




