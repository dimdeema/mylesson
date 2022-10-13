n = int(input('четное число'))
res = str()

for i in str(n):
 if int(i) % 2 == 0:
  res += i

print(res)
