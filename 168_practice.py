import math
y= 7
num = int(input('Enter the nth term of pascal triangle :'))
for i in range(0,num):
    print('\n')
    # y = y - 1
    for a in range(0,i+1):
        n = math.factorial(i)
        r = math.factorial(a)
        p = math.factorial(i-a)
        c = n//(p*r)
        print(c,end=' ')