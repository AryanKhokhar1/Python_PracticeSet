lis = [1,4,6,78,9,4]
new_lis = lis
odd = []
for i in range(len(lis)):
    if(lis[i] % 2 != 0):
        odd.append(lis[i])
print(odd)