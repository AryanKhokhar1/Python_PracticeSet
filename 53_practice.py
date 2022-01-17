a = int(input('Enter the first number :'))
b = int(input('Enter the second number :'))
c = int(input('Enter the third number :'))

if(a<b):
    if(b<c):
        print(c,'is the greatest')
    else:
        print(b,'is the greatest')
else:
    if(a<c):
        print(c,' is the greatest')
    else:
        print(a,'is the greatest')