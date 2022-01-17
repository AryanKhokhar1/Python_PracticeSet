def prime_number(num,a):
    p = a + 1
    if(p == num):
        return 0
    elif(num % p == 0):
        return 1
    return prime_number(num,p)
num = int(input('Enter a number :'))
a = 1
x = prime_number(num , a)
if(x == 1):
    print(num,'is not a prime number')
else:
    print(num,'is a prime number')