def fac(mult,num):
    mult = mult * num
    if(num == 1):
        return mult
    else:
        return fac(mult , num - 1)
mult = 1
num = int(input('Enter the last number of sequence :'))
sum = 0
for i in range(1,num +1):
    p = fac(mult,i)
    sum = sum + p
print('Sum =',sum)