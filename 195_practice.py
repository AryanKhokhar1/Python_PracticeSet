def flatten(lis,a,sum,z):
    v = lis[a]
    if(type(v) == list):
        l = len(v)
        for i in range(0,l):
            r = v[i]
            sum = sum + r
            # print(r,end='+')
    else:
        sum = sum + v
        # print(v,end='+')
    if(a == z):
        return sum
    return flatten(lis,a+1,sum,z)

lis = [1,2,[3,4,5]]
a = 0
l = len(lis) - 1
sum = 0
ans = flatten(lis,a,sum,l)
print('Sum =',ans)