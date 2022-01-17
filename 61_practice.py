days = {
    1 : 'Sunday',
    2 : 'Monday',
    3 : 'Tuesday', 
    4 : 'Wednesday',
    5 : 'Thursday',
    6 : 'Friday',
    7 : 'Saturday',
}
a = int(input('Enter the day in numberic :'))
if(a>7):
    a = a % 7
print(days[a])