n = int(input('Enter the number of elements in dictionary: '))
lis1 = []
lis2 = []
for i in range(n):
    a = input(f'Enter the {i+1} element: ')
    lis1.append(a[0])
    lis2.append(a)
d = dict(zip(lis1,lis2))
print('The dictionary =',d)