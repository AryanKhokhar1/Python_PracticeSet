h = input('Enter the Hexadecimal Number :')
num = int(h,16)
# print('Decimal value =',num)
num = bin(num)
print('Binary Number =',num[2:])