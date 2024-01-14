class word:
    def join(self):
        return self.start
    def split(self,l):
        f = len(self.start)
        for i in range(0,l):
            print(self.start[i],end='')
        print('')
        for i in range(l,f):
            print(self.start[i],end='')
        return
        
a = word()
a.start = input('Enter the First String :')
s = int(input('Enter the position of string to split :'))
print('Split of two string :')
a.split(s)
print('\nJoin of two string :\n',a.join())
