num = int(input('Binary Number ='))
sum = 0
a = 0
while(num > 0):
    d = num % 10
    num = num // 10
    sum = sum + d*(2**(a))
    a = a + 1
print('Decimal value =',sum)