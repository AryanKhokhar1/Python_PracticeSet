r = input('Enter the Roman Number(small letter) :')
l = len(r)
# t = 0
# while(t != l):
if('xxxx' in r or 'iiii' in r or 'vv' in r or 'll' in r or 'cccc' in r or'dd' in r ):
    print('Error! Given Roman number is invalid')
else:
    if