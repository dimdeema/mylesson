# Калькулятор. Пользователь вводит с клавиатуры числа и операцию и получает результат.

a = float(input('Введите первое дробное число: '))
c = input('Введите операцию(+, -, *, /):')
b = float(input('Введите второе дробное число:'))

if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
else:
    print(a/b)

