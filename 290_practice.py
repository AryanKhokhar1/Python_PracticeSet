tup = (1,5,67,4,3,2)
n = int(input('Enter the index: '))
if(n>len(tup)-1):
    n = len(tup) - 1
elif(n < 0):
    n = 0
print(tup[n])