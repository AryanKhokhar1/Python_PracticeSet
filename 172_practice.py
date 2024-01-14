def square(num,lis):
    if(num == 31):
        return lis
    else:
        p = num**(2)
        lis.append(p)
        return square(num+1,lis)
lis = list()
i = 1
ans = square(i,lis)
print(ans)
