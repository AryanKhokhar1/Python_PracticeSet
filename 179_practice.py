def sequence(a,b,r,num):
    sum = a + b
    a = b
    b = sum
    r = r + 1
    if(r == num):
        print(sum)
    else:
        print(sum,end=',')
    if(r == num):
        return
    else:
        return sequence(a,b,r,num)
num = int(input('Enter the range of fibonacci series :'))
r = 0
print(0,end=',')
print(1,end=',')
sequence(0,1,r,num)