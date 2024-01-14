def factorial(number,fac):
    fac = fac * number
    if(number == 2):
        return fac
    else:
        return factorial(number -1 , fac)
num = int(input('Enter the Number for factorial :'))
mult = 1
ans = factorial(num,mult)
print('Factorial =',ans)