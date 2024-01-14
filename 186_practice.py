def binary():
    num = input('Enter the Number :')
    if(num == 'Stop' or num == 'stop'or num == 's'):
        return
    else:
        num = int(num)
        num = bin(num)
        print('Binary Number =',num[2:])
    return binary()
print('For stop transforming deal (s),(stop)or(Stop)')
binary()