from re import A


a = int(input('Enter the cofficient of x^2 :'))
b = int(input('Enter the cofficient of x :'))
c = int(input('Enter the value of constant :'))
d = (b**(2)-4*a*c)**(0.5)
x1 = (-b + d)/2*a
x2 = (-b - d)/2*a
print('First root =',x1)
print('Second root =',x2)