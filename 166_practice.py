# perfect Number 
def perfect_check(num ,n,lis):
    if(n == 0):
        return lis
    if(num % n == 0):
        lis.append(n)
    return perfect_check(num,n-1,lis)
num = int(input('Enter the Number(for checking it Perfect Number) : '))
n = num - 1
lis = list()
ans = perfect_check(num , n,lis)
l = len(ans)
# print(ans)
sum = 0
for i in range(0,l):
    p = lis[i]
    sum = sum + p
    if(i == (l - 1)):
        print(p,end=' ')
    else:
        print(p,end='+')
if(num == sum):
    print('=',num,'is the perfect Number')
else:
    print('!=',num,'is not perfect Number')