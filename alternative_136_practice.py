# This program will change binary number to Octal number
num = int(input('Binary Number :'))
ans = []
z = ''
n = ''
while(num > 0):
    ans.append(num % 1000)
    num = num // 1000
l = len(ans)
# print(ans , l)
for i in range(0,l):
    r = 0
    p = ans[i]
    t = str(p)
    y = len(t)
    p = int(p)
    for a in range(0,y):
        d = p % 10
        p = p // 10
        r = r + d*(2**(a))
    z = z + str(r)
z = int(z)
# print(type(z))
# print(z)
Reverse = 0
while(z > 0):
    Reminder = z %10
    Reverse = (Reverse *10) + Reminder
    z = z //10
print("Octal Number " ,Reverse)