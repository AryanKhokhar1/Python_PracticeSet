def flatten(lis,a,ne,z):
    v = lis[a]
    if(type(v) == list):
        l = len(v)
        for i in range(0,l):
            r = v[i]
            ne.append(r)
    else:
        ne.append(v)
    if(a == z):
        return ne
    return flatten(lis,a+1,ne,z)

lis = [1,2,[3,4,5,5,6],6,[5,6,8]]
a = 0
l = len(lis) - 1
ne = list()
ans = flatten(lis,a,ne,l)
print(ans)