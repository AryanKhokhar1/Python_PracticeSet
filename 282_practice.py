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
c11 = [r21[0],r22[0],r23[0]]
c12 = [r21[1],r22[1],r23[1]]
c13 = [r21[2],r22[2],r23[2]]
a = 0
output1 = []
for i in range(3):
    a = a + (r11[i]*c11[i])
output1.append(a)
a = 0
for i in range(3):
    a = a + (r11[i]*c12[i])
output1.append(a)
a = 0
for i in range(3):
    a = a + (r11[i]*c13[i])
output1.append(a)
output2 = []
a = 0
for i in range(3):
    a = a + (r12[i]*c11[i])
output2.append(a)
a = 0
for i in range(3):
    a = a + (r12[i]*c12[i])
output2.append(a)
a = 0
for i in range(3):
    a = a + (r12[i]*c13[i])
output2.append(a)
output3 = []
a = 0
for i in range(3):
    a = a + (r13[i]*c11[i])
output3.append(a)
a = 0
for i in range(3):
    a = a + (r13[i]*c12[i])
output3.append(a)
a = 0
for i in range(3):
    a = a + (r13[i]*c13[i])
output3.append(a)
print(f"""{output1}
{output2}
{output3}""")