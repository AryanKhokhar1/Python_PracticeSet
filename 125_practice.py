
num = int(input('Enter the last term of the sequence :'))
sum = 0
for i in range(1,num + 1):
    for a in range(1,i+1):
        sum = sum + (a)

print('Sum of the sequence =',sum)