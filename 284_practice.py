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
print('---------Transpose of matrix----------')
for i in range(3):
    print('               ',r11[i],r12[i],r13[i])