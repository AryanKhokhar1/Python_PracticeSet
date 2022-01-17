num = int(input('Binary Number ='))
sum = 0
a = 0
r = ''
lis = []
while(num > 0):
    d = num % 10
    num = num // 10
    sum = sum + d*(2**(a))
    a = a + 1
# print('Decimal value =',sum)

while(sum>0):
    p = sum % 16
    if(p == 10):
        p = 'A'
    elif(p == 11):
        p = 'B'
    elif(p == 12):
        p = 'C'
    elif(p == 13):
        p = 'D'
    elif(p == 14):
        p = 'E'
    elif(p == 15):
        p = 'F'
    sum = sum // 16
    lis.append(p)
    # print(p)
p = (lis[-1::-1])
# print(type(p)) --> p is a list
print('Hexa Decimal Number=',p)
