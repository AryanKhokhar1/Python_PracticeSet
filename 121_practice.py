def addition(num ,l1):
    num = num * 2
    l1.append(num)
    # print(num)
    if(num == 64):
        return l1
    else:
        return addition(num,l1)
num =1
l1 = [1,]
ans = addition(num ,l1)
print(ans)