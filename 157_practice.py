def addition(lis,n,sum):
    sum = sum + lis[n]
    if(n == 0):
        return sum
    else:
        return addition(lis,n-1 ,sum)
lis = [5,6]
n= len(lis) - 1
sum = 0
ans = addition(lis,n,sum)
print('Addition of all elements of List =',ans)