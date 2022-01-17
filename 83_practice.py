print('This program is for Combination')
n = int(input('Enter the value of n :'))
r = int(input('Enter the value of r :'))
x = (n -r)
fac_n = 1
fac_r = 1
fac_x = 1
for i in range(n,0,-1):
    fac_n = fac_n * i
for i in range(r,0,-1):
    fac_r = fac_r * i
for i in range(x,0,-1):
    fac_x = fac_x * i
print('Combination =',fac_n/(fac_x * fac_r))