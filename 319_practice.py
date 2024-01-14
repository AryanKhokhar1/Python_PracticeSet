f = open('store.txt','r')
n = input('Enter the word: ')
store = f.read()
store = store.split(' ')
a = 1
pr = 0
for i in store:
    if('\n' in i):
        a = a + 1
    elif(n == i):
        pr = 1
        break
if(pr == 0):
    print(f"'{n}' is not present in the file")
else:
    print(f"'{n}' is present in {a} line")