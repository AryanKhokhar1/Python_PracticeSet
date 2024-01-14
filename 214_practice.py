class string:
    def check(self,l):
        for i in range(0,l):
            v = self.story[i]
            n = self.story.count(v)
            if(n<3):
                print(v,end=',')
a = string()
a.story = input('Enter the story :')
l = len(a.story)
a.check(l)