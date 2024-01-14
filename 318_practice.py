f = open('store.txt','r')
store = f.read()
a = 0
for i in store:
    if(i == 'n'):
        a = a + 1
print('Total numbers of n in sentence =',a)