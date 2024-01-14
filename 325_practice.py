f = open('file1.txt','r')
store = f.readlines()
a = open('file3.txt','w')
for i in range(len(store)):
    if(i%2 == 0):
        a.write(store[i])