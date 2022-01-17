len1 = float(input('Enter the length of first side of triangle :'))
len2 = float(input('Enter the length of second side of triangle :'))
len3 = float(input('Enter the length of third side of triangle :'))
semi_perimeter = (len1 + len2 + len3)/2
Area = (semi_perimeter*(semi_perimeter - len1)*(semi_perimeter - len2)*(semi_perimeter - len3))**(0.5)
print('Area of triangle =',Area)