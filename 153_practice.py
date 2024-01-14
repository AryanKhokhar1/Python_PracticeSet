num = int(input('Enter the Number :'))
p = str(num)
sum = ''
while(num > 0):
    d = num % 10
    num = num // 10
    sum = sum + str(d)
if(p == sum):
    print(sum,'is a palindrome Number')
else:
    print(p,'is not a palindrome Number ')