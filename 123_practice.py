def addition(num):
    sum = 0
    for i in range(1,num + 1):
        sum = sum + i
    return sum
num = int(input('Enter the term of sequence :'))
# p = 0
# n = int(input('Enter the last digit of sequence :'))
ans = addition(num)
print('Sum =',ans)