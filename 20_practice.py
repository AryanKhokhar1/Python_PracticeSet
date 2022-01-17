print('This program used for finding perimeter of Circle,Rectangle and Triangle')
# Perimeter is the sum of all side for perticular figure
# Circle
radius = float(input('Enter the radius of Circle :'))
print('Perimeter of Circle =',2*(22/7)*radius)
# Rectangle
length = float(input('Enter the length of rectangle :'))
width = float(input('Enter the width of rectangle :'))
print('Perimeter of Rectangle =',2*(length + width))
# Triangle
side1 = float(input('Enter the length of first side :'))
side2 = float(input('Enter the length of second side :'))
side3 = float(input('Enter the length of third side :'))
print('Perimeter fo triangle =',side1 + side2 + side3)