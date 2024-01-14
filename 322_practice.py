f = open('test.txt','r')
store = f.readlines()
lis = []
for i in store:
    if i not in lis:
        lis.append(i)
print(lis)