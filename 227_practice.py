class excution:
    company = 'GOOGLE'
    def fstring(self):
        print(f'{self.name} is working in {self.company}')
employee = excution()
employee.name = input('Enter your name :')
employee.fstring()