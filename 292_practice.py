tup = (1,'abc',6,7,4,'a','z')
lis = []
for ele in tup:
    if(type(ele) == int):
        lis.append(ele)
print('Number =',lis)