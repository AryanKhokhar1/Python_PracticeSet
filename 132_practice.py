
# a = 1
num = int(input('Enter the nth term of the sequence :'))
l1 = [1]
for i in range(1,num+1):
    if(i % 2 != 0):
        l1.append(2*l1[i-1])
    else:
        l1.append(l1[i-1] + l1[i-2])
print('Sequence =',l1)