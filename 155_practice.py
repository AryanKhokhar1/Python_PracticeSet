
num = int(input('Enter the last Number of the Series :'))
p = num
sum = 0
for i in range(1,num + 1):
    sum = sum + i
    if(i == num):
        print(i,end= '')
    else:
        print(i, end=' + ')
print(' =',sum)