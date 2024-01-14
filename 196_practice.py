def length(lis,a):
    if(not lis):
        return a
    else:
        r = lis[a]
        lis.remove(r)
        a = a + 1
    return length(lis,a)
lis = [1,3,5,[6,8,4]]
a = 0
ans = length(lis,a)
print('Length =',ans)