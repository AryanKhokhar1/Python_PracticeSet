f = open('data.txt','r')
n = int(input('Enter the range of file material display: '))
store = f.read()
for i in range(n):
    print(i)