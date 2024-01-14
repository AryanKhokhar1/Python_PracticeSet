num1 = int(input('Enter the First Number :'))
num2 = int(input('Enter the Second Number :'))
mult = 1
if(num1<= num2):
    b = num1
else:
    b = num2
i = 2
while(b >= i):
    if(num1 % i == 0 and num2 % i == 0):
        num1 =num1 // i 
        num2 = num2 // i
        mult = mult * i
    else:
        i += 1
print('HCF =',mult)