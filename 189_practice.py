def check_prime(num,a):
    if(num <= a):
        return 0
    else:
        if(num % a == 0):
            return 1
        else:
            return check_prime(num,a+1)
num = int(input('Enter a Number for check (prime condition) :'))
a = 2
ans = check_prime(num,a)
if(ans == 0):
    print(num,'is a Prime Number ')
else:
    print(num,'is not a Prime Number ')