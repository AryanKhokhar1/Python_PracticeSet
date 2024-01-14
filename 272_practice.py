lis = [1,-3,-6,-9,7,8,4,12,-1]
n1 = int(input('Enter the starting point: '))
n2 = int(input('Enter the ending point: '))
negative = []
for digit in lis:
    if(digit >= n1 and digit <= n2):
        negative.append(digit)
negative.sort()
print('Negative number at given range =',negative)