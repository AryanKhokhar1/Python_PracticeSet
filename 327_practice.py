f = open('store.txt','r')
store = f.readline()
for i in range(len(store)-1,-1,-1):
    print(store[i],end='')