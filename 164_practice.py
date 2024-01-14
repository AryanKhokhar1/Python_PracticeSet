
def prime_check(num,n):
    if(n == 1 or n == 2):
        return 0
    if(num % n == 0):
        return 1
    else:
        if(n == 2):
            return 0
        else:
            return(prime_check(num , n - 1 ))
num = int(input('Enter the Number(for check prime:)'))
n = num - 1
ans = prime_check(num ,n)

if(ans == 0 or ans == None ):
    print(num,'is a prime Number')
else:
    print(num,'is not a prime Number')