
num = int(input('Enter the last digit of sequence :'))
sum = 0
for i in range(1,num +1):
    sum = sum + (i**i)
print('Sum = ',sum)