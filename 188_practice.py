def HCF(num1,num2,b,a,mult):
    if(num1 % a == 0 and num2 % a == 0):
        mult = mult * a
        num1 = num1 // a
        num2 = num2 // a
    else:
        a = a + 1
    if(a == b):
        return mult
    else:
        return HCF(num1,num2,b,a,mult)
num1 = int(input('Enter the First Number :'))
num2 = int(input('Enter the Second Number :'))
a = 2
mult = 1
if(num1 <= num2):
    b = num1
else:
    b = num2
ans = HCF(num1,num2,b,a,mult)
print(f'GCD of {num1} and {num2} = {ans}')