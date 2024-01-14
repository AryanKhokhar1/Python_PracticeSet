lis = [1,4,6,78,9,4]
for digit in lis:
    if(digit % 2 != 0):
        lis.remove(digit)
print(lis)