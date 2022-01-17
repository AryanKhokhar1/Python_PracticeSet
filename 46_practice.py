a = float(input('Enter the first number :'))
b = float(input('Enter the second number :'))
if(a<b):
    print(f'{b} is the greatest')
elif(b<a):
    print(f'{a} is the greatest')
else:
    print(f'Both are equal')