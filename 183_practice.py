def check(n):
    num = int(input('Enter the Number :'))
    if(num % 2 == 0):
        print(num,'is a even Number')
    else:
        print(num,'is a odd Number')
    if(n == 0):
        return
    else:
        return check(n-1)

n = 10
check(10)