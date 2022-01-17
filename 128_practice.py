def fac(num,mult):
    mult = mult * num
    if(num == 1):
        return mult
    else:
        return fac(num - 1,mult)
    
num = int(input('Enter the last number of sequence :'))
sum = 0
mult = 1
for i in range(1,num + 1):
    p = fac(i,mult)
    sum = sum + (p/i)
print('Sum =',sum)