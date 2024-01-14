
def change(lis):
    lis = set(lis)
    lis = list(lis)
    return lis
lis = []
l = int(input('Enter the No of List :'))
for i in range(0,l):
    a = int(input('Enter the number :'))
    lis.append(a)
ans = change(lis)
print(ans)