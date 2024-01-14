lis = [1,3,4,6,8,9]
n = int(input('Enter the position to break list: '))
a = 0
new_list1 = []
new_list2 = []
for i in range(n):
    new_list1.append(lis[i])
for i in range(n,len(lis)):
    new_list2.append(lis[i])
print('The First list =',new_list1)
print('The Second list =',new_list2)