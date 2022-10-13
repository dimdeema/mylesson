a = int(input('введите год'))
if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
    print('невисокосный')
else:
    print('високосный')
