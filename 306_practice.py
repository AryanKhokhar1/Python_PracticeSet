dict1 = {1:23, 2:454, 3:68}
n = int(input('Enter the key for check: '))
key = []
for k in dict1.keys():
    key.append(k)
if(n in key):
    print(n,'is present in the dictionary')
else:
    print(n,'is not present in the dictionary')