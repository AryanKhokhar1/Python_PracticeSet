
n = int(input('Enter the number: '))
lis1 = []
lis2 = []
for i in range(1,n+1):
    lis1.append(i)
    lis2.append(i**2)
d = dict(zip(lis1,lis2))
print(d)