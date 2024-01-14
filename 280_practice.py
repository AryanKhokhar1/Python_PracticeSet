print('Give value of list 1')
r11 = []
for i in range(3):
    a = int(input(f'Enter the {i+1} element of row1 ='))
    r11.append(a)
r12 = []
for i in range(3):
    a = int(input(f'Enter the {i+1} element of row2 ='))
    r12.append(a)
r13 = []
for i in range(3):
    a = int(input(f'Enter the {i+1} element of row3 ='))
    r13.append(a)
print('Give the value of list 2')
r21 = []
for i in range(3):
    a = int(input(f'Enter the {i+1} element of row1 ='))
    r21.append(a)
r22 = []
for i in range(3):
    a = int(input(f'Enter the {i+1} element of row2 ='))
    r22.append(a)
r23 = []
for i in range(3):
    a = int(input(f'Enter the {i+1} element of row3 ='))
    r23.append(a)
for i in range(3):
    print(r11[i]+r21[i],end =' ')
print()
for i in range(3):
    print(r12[i]+r22[i],end =' ')
print()
for i in range(3):
    print(r13[i]+r23[i],end =' ')