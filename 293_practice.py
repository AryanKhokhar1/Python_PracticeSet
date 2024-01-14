def tup(tup1,tup2):
    return tup1,tup2
tup1 = (1,2,4,64,3)
tup2 = (1,5,7,3,2)
lis = []
for i in range(len(tup1)):
    ans = tup(tup1[i],tup2[i])
    lis.append(ans)
print(tuple(lis))