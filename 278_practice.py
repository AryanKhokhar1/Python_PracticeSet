lis = [11,3,5,7,4]
new_lis = []
sum = 0
for i in range(len(lis)):
    sum = sum + lis[i]
    new_lis.append(sum)
print('The cumutative sum =',new_lis)