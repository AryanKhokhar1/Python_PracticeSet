# from math import lcm
# num1 = int(input('Enter the first Number :'))
# num2 = int(input('Enter the second Number :'))
# a = lcm(num1,num2)
# print(a)

num1 = int(input('Enter the first Number :'))
num2 = int(input('Enter the second Number :'))
mult = 1
if(num1 >= num2):
    b = num1
else:
    b = num2
i = 2
while(b >= i):
    if(num1 % i == 0 and num2 % i == 0):
        num1 = num1 //i
        num2 = num2 // i
        mult = mult * i
    elif(num1 % i == 0):
        num1 = num1 // i
        mult = mult * i
    elif(num2 % i == 0):
        num2 = num2 //i
        mult = mult * i
    else:
        i = i + 1
print('LCM =',mult)