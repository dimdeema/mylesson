a = int(input('введите первое число:'))
b = int(input('введите второе число:'))
c = a + 1
while (c < b) and (c < 0):
    print(c)
    c = c + 1
    if (b < c) and (c > 0):
        print(c)