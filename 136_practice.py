num = int(input('Binary Number ='))
sum = 0
a = 0
r = ''
z = ''
while(num > 0):
    d = num % 10
    num = num // 10
    sum = sum + d*(2**(a))
    a = a + 1
print('Decimal value =',sum)

while(sum>0):
    p = sum % 8
    sum = sum // 8
    r = r + str(p)
r = int(r)
while(r>0):
    rem = r % 10
    r = r // 10
    z = z + str(rem)
z = int(z)
print(z)