num = int(input('Enter the Number :'))
sum = 0
while(num > 0):
    d = num % 10
    num = num // 10
    sum = sum + d
print('Sum of digit of the Number =',sum)