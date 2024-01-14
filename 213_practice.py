class string:
    def remove(self,l):
        for i in range(0,l):
            v = self.story[i]
            c = self.story.count(v)
            if(c == 1):
                print(v,end='')
            elif(c>1):
                print(v,end='')
                self.story = self.story.replace(v,' ')


a = string()
a.story = input('Enter the String :')
l = len(a.story)
a.remove(l)