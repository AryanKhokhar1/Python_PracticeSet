import string
# Description about the program
print('Small letter is count as minor then Capital Letter')
num = int(input('Enter the Number of word you want to writer :'))
lis = list()
fil = list()
ne = list()
for i in range(0,num):
    a = input('Enter Words :')
    s = a[0]
    fil.append(s)
    lis.append(a)
for i in string.ascii_letters:
    for a in range(0,num):
        n = fil[a]
        nl = lis[a]
        if(i == n):
            ne.append(nl)
# print(ne)
for i in range(0,num):
    alag = ne[i]
    if(i == (num - 1)):
        print(alag)
    else:
        print(alag,end='-')
# green-red-yellow-black-white