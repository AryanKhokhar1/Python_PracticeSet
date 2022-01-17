print('1 is a prime number')
print('2 is a prime number')
sum = 3
for i in range(2,1001):
    x = 0
    for a in range(2,i):
        if(a+1 == i):
            print(i,'is a prime number')
            sum = sum + i
            break
        elif(i % a == 0):
            x = 1
            print(i,'is not a prime number')
            break
print('Sum of 1000 natural number =',sum)