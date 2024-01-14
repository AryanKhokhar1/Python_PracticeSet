num = int(input('Enter the range sequence :'))
i = 0
sum = 0
while (num > sum +1):
    sum = 2*i + 1
    
    if (num <= sum +1):
        print(sum)
        i = i + 1
    else:
        print(sum ,end ="," )
        i = i + 1