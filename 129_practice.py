num = int(input('Enter the last number of sequence :'))
sum = 0
for i in range(1,num+1):
    sum = sum + (i**i)/i
print('Sum =',sum)