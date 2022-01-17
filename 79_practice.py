num = int(input('Enter the number :'))
p = num
l = len(str(num))
sum = 0
while(num > 0):
    d = num % 10
    num = num // 10
    sum = sum + d**(l)
    l = l -1
print(f'Disarium Number of {p} = {sum}')