str1 = input('Enter the 1st string: ')
str2 = input('Enter the 2nd string: ')
lis = []
for i in str2:
    if(i not in str1):
        lis.append(i)
print('Letter in 2nd string but not in 1st string:',lis)