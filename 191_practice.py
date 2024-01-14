def power(num,n,a,mult):
    if(n == 0):
        return 1
    elif(n == a):
        return mult
    else:
        mult = mult * num
    return power(num,n,a+1,mult)
num = int(input('Enter the Number :'))
n = int(input('Enter the power of Number :'))
a = 0
mult = 1
ans = power(num,n,a,mult)
print(f'Answer = {ans}')