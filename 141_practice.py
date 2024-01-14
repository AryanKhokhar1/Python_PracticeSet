o = (input('Enter the Octal Number :'))
num = int(o,8)
# In below line num is decimal value of Octal Number
# print(num)
num = bin(num)
print('Binary Number =',num[2:])