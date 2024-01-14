lis = [1,2,3,5,7,3,35,1,3,2,2,4]
new_lis = []
for i in lis:
    if(lis.count(i)>1):
        new_lis.append(i)
new_lis = set(new_lis)
new_lis = list(new_lis)
print('Duplicate elements =',new_lis)