year = int(input('Enter the year :'))
if(year % 100 == 0):
    if(year % 400 == 0):
        print(year,'is a leap year')
    else:
        print(year,'isn\'t leap year')
else:
    if(year % 4 == 0):
        print(year,'is a leap year')
    else:
        print(year,'isn\'t a leap year')