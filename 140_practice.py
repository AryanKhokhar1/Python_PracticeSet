rn = input('Enter the ROMAN NUMBER(small letter) :')
a = []
# This will use to split string into list
a[:] = rn
l = len(a)
sum = 0
i = 0
# print(l)
while(i != l):
    # Errors
    if(a[i:i+5] == ['x','x','x','x']):
        print('Error! You type something wrong')
        break
    elif(a[i:i+2] == ['v','v']):
        print('Error! You type something wrong')
        break
    elif(a[i:i+5] == ['i','i','i','i']):
        print('Error! You type something wrong')
        break
    elif(a[i:i+2] == ['l','l']):
        print('Error! You type something wrong')
        break
    elif(a[i:i+5] == ['c','c','c','c']):
        print('Error! You type something wrong')
        break
    elif(a[i:i+2] == ['i','v'] or a[i:i+2] == ['I',"V"]):
        v = 4
    elif(a[i] == 'x' or a[i] == 'X'):
        v = 10
    elif(a[i] == 'v' or a[i] == 'V'):
        v = 5
    elif(a[i] == 'i' or a[i] =='I'):
        v = 1
    sum = sum + v
print('Value =',sum)


