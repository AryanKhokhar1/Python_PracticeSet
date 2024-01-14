def multiply(lis,n,mult):
    mult = mult * lis[n]
    if(n == 0):
        return mult
    else:
        return multiply(lis,n-1,mult)
lis = [2,3,5,4]
l = len(lis) - 1
mult = 1
ans = multiply(lis,l,mult)
print('The multiplication of all elements in lists =',ans)