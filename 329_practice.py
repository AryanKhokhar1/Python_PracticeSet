f = open('new_file.txt','r')
store = f.read()
store = store[::-1]
f.close()
f = open('new_file.txt','w')
f.seek(0)
f.write(store)
f.close()