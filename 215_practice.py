class string:
    def check(self,l,i):
        while(i != l):
            v = self.story[i]
            n = self.story.count(v)
            if(n>3):
                print(v,end=',')
                self.story = self.story.replace(v,'')
                i = i + n 
            else:
                i = i + 1
a = string()
a.story = input('Enter the story :')
l = len(a.story)
i = 0
a.check(l,i)