str1 = input('Enter the 1st string: ')
str2 = input('Enter the 2nd string: ')
lis = []
for i in str1:
    if(i not in str2):
        lis.append(i)
print('Letter in 1st string but not in 2nd string:',lis)