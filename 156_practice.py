def maximum(a,b,c):
    if(a>b):
        if(a>c):
            print(a,'is the greatest')
        else:
            print(c,'is the greatest')
    else:
        if(b>c):
            print(b,'is the greatest')
        else:
            print(c,'is the greatest')
a = int(input('Enter the First Number :'))
b = int(input('Enter the Second Number :'))
c = int(input('Enter the Third Number :'))
maximum(a,b,c)