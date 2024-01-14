print('Give the value of list 1')
r11 = []
for i in range(2):
    a =int(input(f'Enter the {i+1} element of row 1: '))
    r11.append(a)
r12 = []
for i in range(2):
    a = int(input(f'Enter the {i+1} element of row 2: '))
    r12.append(a)
print('Give the value of list 2')
r21 = []
for i in range(2):
    a =int(input(f'Enter the {i+1} element of row 1: '))
    r21.append(a)
r22 = []
for i in range(2):
    a =int(input(f'Enter the {i+1} element of row 2: '))
    r22.append(a)
c11 = [r21[0],r22[0]]
c12 = [r21[1],r22[1]]
a = 0
for i in range(2):
    a = a + (r11[i]*c11[i])
b = 0
for i in range(2):
    b = b + (r11[i]*c12[i])
c = 0
for i in range(2):
    c = c + (r12[i]*c11[i])
d = 0
for i in range(2):
    d = d + (r12[i]*c12[i])
print(a,b)
print(c,d)