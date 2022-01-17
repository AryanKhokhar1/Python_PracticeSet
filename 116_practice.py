
def multiple(num , n, seq):
    seq[n] = num * n
    # print(seq)
    if(n == 5):
        return seq
    return multiple(num , n+1 ,seq)
num = 5
a = 0
seq= [1,1,1,1,1,1]
a = multiple(num , a ,seq)
print(tuple(a))