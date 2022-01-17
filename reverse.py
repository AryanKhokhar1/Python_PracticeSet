z = 31
n = ''
while(z>0):
    g = z % 10
    z = z // 10
    g = str(g)
    n = n + (g)
print('Octal Number =',n)

# Python Program to Reverse a Number using While loop.
# Number = int(input("Please Enter any Number: "))
# Reverse = 0
# while(Number > 0):
#     Reminder = Number %10
#     Reverse = (Reverse *10) + Reminder
#     Number = Number //10
# print("\n Reverse of entered number is = %d" %Reverse)