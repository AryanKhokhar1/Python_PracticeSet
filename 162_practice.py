import string
story = input('Enter the string :')
l = len(story)
a = 0
b = 0
c = 0
for i in range(0,l):
    if(story[i] in string.ascii_lowercase):
        a = a + 1
    elif(story[i] in string.ascii_uppercase):
        b = b + 1
    else:
        c = c + 1
print(f'Contain {a} small letter')
print(f'Contain {b} Upper letter')
print(f'Contain {c} digit and symbol and space')