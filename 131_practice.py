def positive(num):
    # print(num/num+1)
    return (num/(num+1))
def negative(num):
    return -(num/(num+1))

num = int(input('Enter the last number of sequence :'))

sum1 = 0
sum2 = 0 
# fake = 1
for i in range(1,num + 1):
    if(i % 2 == 0):
        n = negative(i)
        sum2 = sum2 + n
    else:
        p = positive(i)
        sum1 = sum1 + p
print(sum1)
print(sum2)
print('Sum =',sum2 + sum1)