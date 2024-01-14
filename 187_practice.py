def LCM(num1,num2,mult,b,a):
    if(num1 % a == 0 and num2 % a == 0):
        num1 = num1 // a 
        num2 = num2 // a
        mult = mult * a
    elif(num1 % a == 0):
        num1 = num1 // a 
        mult = mult * a
    elif(num2 % a == 0):
        num2 = num2 // a 
        mult = mult * a
    else:
        a = a + 1
    
    if(a == b):
        return mult
    else:
        return LCM(num1,num2,mult,b,a)


num1 = int(input('Enter the first Number :'))
num2 = int(input('Enter the second Number :'))
mult = 1
a = 2
if(num1>= num2):
    b = num1
else:    
    b = num2
ans = LCM(num1,num2,mult,b,a)
print(f'LCM of {num1} and {num2} = {ans}')