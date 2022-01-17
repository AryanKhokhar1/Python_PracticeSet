num = int(input('Enter a number :'))
p = num
sum = 0
while(num > 0):
    d = num % 10
    num = num // 10
    sum = sum + d
if(p % sum == 0):
    print(p,'is a Harshad Number')
else:
    print(p,'is not a Harshad number')