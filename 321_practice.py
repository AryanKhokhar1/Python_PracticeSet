f = open('file.txt','r')
store = f.readlines()
for i in store:
    if(i[0] == 'a' or i[0:2] == 'an'):
        pass
    else:
        print(i)