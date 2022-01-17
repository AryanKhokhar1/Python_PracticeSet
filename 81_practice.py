num = int(input('Enter a number to find it\'s Armstrong Number:'))
s = len(str(num))
sum = 0
while(num > 0):
    d = num % 10
    num = num // 10
    sum = sum + d**(s)
print('Armstrong number =',sum)