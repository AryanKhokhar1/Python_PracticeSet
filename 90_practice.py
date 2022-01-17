print('1 is a prime number')
print('2 is a prime number')
for i in range(2,501):
    x = 0
    for a in range(2,i):
        if(a+1 == i):
            print(i,'is a prime number')
            break
        elif(i % a == 0):
            x = 1
            print(i,'is not a prime number')
            break
