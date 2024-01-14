lis = []

for i in range(2):
    new_lis = []
    a = int(input('Enter the number: '))
    new_lis.append(a)
    new_lis.append(a**3)
    new_tup = tuple(new_lis)
    lis.append(new_tup)
print(lis)