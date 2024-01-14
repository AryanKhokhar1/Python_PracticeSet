def tower(num,r):
    txt = (' *'*num)
    t = txt.center(70)
    print(t)
    if(r == num):
        return
    else:
        return tower(num + 1,r)
r = int(input('Enter the range of Tower :'))
num = 1
tower(num,r)
