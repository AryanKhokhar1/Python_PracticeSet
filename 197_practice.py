class Addition:
    def sum(self):
        return self.num1 + self.num2
a = Addition()
a.num1 = int(input('Enter the First Number :'))
a.num2 = int(input('Enter the Second Number :'))
s = a.sum()
print('Sum =',s)