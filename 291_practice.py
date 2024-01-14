tup1 = (1,3,4,64,6,4)
tup2 = (1,3,4,64,6,34)
new_tuple = tuple()
for i in tup2:
    if i not in tup1:
        tup1 = list(tup1)
        tup1.append(i)
print(tup1)