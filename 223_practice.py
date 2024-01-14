class duplicate:
    def make_list(self):
        s = ''
        lis = list()
        l = len(self.story)
        for i in range(0,l):
            v = self.story[i]
            if(v == ' ' ):
                lis.append(s)
                s = ''
            else:
                s = s + v
        return lis
    def replace(self,lis):
        l = len(lis)
        if(self.find in self.story):
            for i in range(0,l):
                if(lis[i] == self.find):
                    lis[i] = self.change
            return lis
        else:
            print(f"There no word '{self.find}' in the Story")

    def display(self,lis):
        l = len(lis)
        for i in range(0,l):
            print(lis[i],end=' ')

a = duplicate()
a.story = input('Fill the story :') + ' '
a.find = input('Find = ')
a.change = input('Replace = ')
lis = a.make_list()
ans = a.replace(lis)
a.display(ans)