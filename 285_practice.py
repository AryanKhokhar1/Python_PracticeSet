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
n = int(input('Enter the coulumn: '))
c11 = [r11[0],r12[0],r13[0]]
c12 = [r11[1],r12[1],r13[1]]
c13 = [r11[2],r12[2],r13[2]]
if(a == 1):
    print(c11)
elif(a == 2):
    print(c12)
elif(a == 3):
    print(c13)
else:
    print('You Type out of index')