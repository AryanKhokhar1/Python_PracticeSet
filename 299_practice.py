word = 'abckdehaidhsahalhfual'
lis = []
for i in word:
    if(i in 'aeiouAEIOU'):
        lis.append(i)
s = set(lis)
print('Total number of vowel in string =',s)