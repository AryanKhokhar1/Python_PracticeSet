from math import remainder


num = int(input('Enter the number :'))
rev = ''
rem = list()
while(num > 0):
    rem = str(num % 10)
    num = num // 10
    rev = rev + rem
print(rev)
# for i in range(1,p+1):
#     print(rem[i])