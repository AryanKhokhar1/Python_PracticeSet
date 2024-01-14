class string():
    def check(self,l,counting):
        for i in range(0,l):
            v = self.story1[i]
            if(v in self.story2):
                counting = counting + 1
                # print(v,end=',')
        if(counting >0 ):
            print(f'There are {counting} matched character')
        else:
            print('There is no matched character')
a = string()
a.story1 = input('Enter the First Story :')
a.story2 = input('Enter the Second Story :')
l = len(a.story1)
counting = 0
a.check(l,counting)
