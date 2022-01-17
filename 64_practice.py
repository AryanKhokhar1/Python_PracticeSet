a = input('Enter specific key for finding area of circle(c),square(s),rectangle(r) or triangle(t)')
if(a =='c'):
    radius = float(input('Enter the value of radius :'))
    print('Area of Circle =',(22/7)*radius*radius)
elif(a == 's'):
    side = float(input('Enter the length of side of square :'))
    print('Area of Square =',side**(2))
elif(a == 'r'):
    length = float(input('Enter the length of rectangle :'))
    width = float(input('Enter the width of rectangle :'))
    print('Area of rectangle =',length*width)
elif(a == 't'):
    import Area_of_triangle_10_practice