num = int(input('Enter the Number :'))
print(f'Checking {num} in 0 to 50 range')
a = 0
for i in range(0,51):
    if(num == i):
        print(f'Yes! {num} lies between 0 to 50')
        a = 1
        break
if(a == 0):
    print(f'{num} is not lies between 0 to 50')