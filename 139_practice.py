sum = int(input('Enter the Decimal Number :'))
lis = []
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
