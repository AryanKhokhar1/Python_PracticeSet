def sequence(num , n, l1):
    l1.append(num * n)
    if(n == 5):
        return l1
    else:
        return sequence(num , n +1, l1)
num = 2
n = 0
l1 =[]
p = sequence(num,n,l1)
print(p)