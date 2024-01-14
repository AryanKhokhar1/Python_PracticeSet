
class Calculator:
    
    def addition(self):
        print('Sum =',self.a + self.b)
    
    def multiply(self):
        print('Multiply =',self.a * self.b)
    
    def Subtraction(self):
        print('Subraction =',self.a - self.b)
    
    def divide(self):
        print('Divide =',self.a /self.b)
c = Calculator()
c.a = float(input('Enter the First Number :'))
c.s = input('Enter the Symbol(+,-,* r /) :')
c.b = float(input('Enter the Second Number :'))
if(c.s == '+'):
    c.addition()
elif(c.s == '-'):
    c.Subtraction()
elif(c.s == '/'):
    c.divide()
elif(c.s == '*'):
    c.multiply()
else:
    print('Given operator is wrong ')