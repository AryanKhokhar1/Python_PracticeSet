
l1 = input('Enter the first Binary Number :')
l2 = input('Enter the second Binary Number :')
num1 = int(l1,2)
num2 = int(l2 ,2)
sum = num1 * num2
sum = bin(sum)
print('Sum of Binary Number =',sum[2:])