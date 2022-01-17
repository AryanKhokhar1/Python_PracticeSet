def addition(n,a,d):
    p = (n/2)*(2*a+(n-1)*d)
    print('Sum of A.P =',p)
a = int(input('Enter the first number of the sequence :'))
d = int(input('Enter the difference between two consicutive number in sequence :'))
n = int(input('Enter the term of the series :'))
p = addition(n,a,d)
