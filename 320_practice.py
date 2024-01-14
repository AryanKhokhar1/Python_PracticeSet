f = open('store.txt','r')
store = f.read()
store = store.split(' ')
b = 1
for i in store:
    if('\n' in i):
        b = b + 1
print('Total number of lines present in file =',b)