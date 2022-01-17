def seq(n , lis,p):
    lis.append(lis[p] + p*13)
    # p = p + 1
    if(n == p):
        return lis
    else:
        return seq(n ,lis , p+1)
num = int(input('Enter the nth term of the sequence :'))
a = 2
p = 0
lis = [2]
ans = seq(num, lis,p)
ans.remove(2)
print('Sequence =',ans)