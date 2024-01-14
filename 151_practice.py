num = int(input('Enter the Number :'))

for i in range(2,num + 1):
    if(num % i == 0):
        print(i,'is the smallest factor of',num)
        break