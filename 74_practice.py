num = int(input('Enter the number for factorial :'))
fac = 1
for i in range(num,0,-1):
    fac = fac * i
print(fac)