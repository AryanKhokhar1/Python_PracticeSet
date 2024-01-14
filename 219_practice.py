class string:
    def character(self,p):
        self.lis[p-1] = ''
        length = len(self.lis)
        for i in range(0,length):
            print(self.lis[i],end='')
a = string()
story = input('Enter the String :')
a.lis = list(story)
p = int(input('Enter the position :'))
a.character(p)