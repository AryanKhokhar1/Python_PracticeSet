def addition(num,l,sum):
    l = l-1
    p = num[l]
    sum = sum + int(p)
    if(l == 0):
        return sum
    else:
        return addition(num,l,sum)
num = (input('Enter the Number :'))
l = len(num)
sum = 0
ans = addition(num,l,sum)
print('Sum of digits =',ans)