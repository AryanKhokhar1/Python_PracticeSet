def addition(lis,l,sum):
    l = l - 1
    p = lis[l]
    sum = sum + p
    if(l == 0):
        return sum
    else:
        return addition(lis,l,sum)

lis = [1,4,35,6,3]
l = len(lis)
print(l)
sum = 0
ans = addition(lis,l,sum)
print('Sum =',ans)