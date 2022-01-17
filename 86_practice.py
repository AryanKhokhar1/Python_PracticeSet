num = int(input('Enter a number for checking palindrome :'))
r = str(num)
rev = ''
while(num != 0):
    d = num % 10
    num  = num // 10
    p = str(d)
    rev = rev + p
# print(rev)
if(r == rev):
    print(r,'is a Palindrome Number')
else:
    print(r,'is not a Palindrome Number')