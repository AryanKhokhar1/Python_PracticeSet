lis = [1,3,5,-5,-9,0,4]
negative = []
for i in range(len(lis)):
    if(lis[i]<0):
        negative.append(lis[i])
print('Postive Number =',negative)