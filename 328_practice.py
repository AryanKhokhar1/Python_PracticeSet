f = open('store.txt','r')
store = f.read()
store = store[::-1]
a = open('new_file.txt','w')
a.write(store)
a.close()
f.close()