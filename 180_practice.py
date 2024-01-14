def addition(num,sum,n):
    sum = sum + num
    if(num == n):
        print(num,end='')
    else:
        print(num,end='+')
    if(num == n):
        return sum
    else:
        return addition(num +1,sum,n)

num = 1
sum = 0
n = int(input('Enter the last Number of the Sequence :'))
ans = addition(num,sum,n)
print(' =',ans)