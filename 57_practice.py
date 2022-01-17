a = input('Enter a digit or number :')
if(a in 'aeious' or a in 'AEIOUS'):
    print(a,'is a vowel')
elif(a in '123456790'):
    print(a,'is a number')
else:
    print(a,'is a consonant')