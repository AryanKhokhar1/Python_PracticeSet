import re
from turtle import circle


class Circle:
    # In below function return does not matter
    def perimeter(self):
        print('Perimeter of Circle =',2*(22/7)*self.r)
        # return
    def Area(self):
        print('Area of Circle =',(22/7)*self.r*self.r)
        # return
c = Circle()
c.r = float(input('Enter the radius of Circle :'))
c.perimeter()
c.Area()