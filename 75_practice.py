num = int(input('Enter the number for factorial :'))
fac = 1

while(num != 0):
    fac = fac * num
    num = num - 1
print(fac)