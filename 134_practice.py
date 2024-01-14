num = int(input('Enter the terms of sequence :'))
a = 1
b = 3
c = 4
print(a,b,end = ',')
for i in range(3,num+1):
    sum = a + b + c
    if (i == num ):
        print(sum)
        break
    else:
        print(sum,end = ',')
        a = b
        b = c
        c = sum