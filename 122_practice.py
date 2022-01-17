def sequence(num , l1):
    num = num + 2
    l1.append(num)
    # print(l1)
    if(num == 8):
        return l1
    else:
        return sequence(num , l1)
num = -10
l1 = []
ans = sequence(num , l1)
print(ans)