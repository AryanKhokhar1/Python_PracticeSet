lis = [2,3,5,7,3,6,78]
n1 = int(input('Enter the starting range: '))
n2 = int(input('Enter the ending range: '))
odd = []
for i in range(n1-1,n2+1):
    if(lis[i] % 2 != 0):
        odd.append(lis[i])
print('The even number list =',odd)