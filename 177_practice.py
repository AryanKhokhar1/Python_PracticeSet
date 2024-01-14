def factorial(num,mult):
    mult = mult *num
    if num == 1:
        return mult
    else:
        return factorial(num -1,mult)

num = int(input('Enter the Number :'))
mult = 1
ans = factorial(num,mult)
print(f'Factorial = {ans}')