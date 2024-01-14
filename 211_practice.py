class string:
    def length_word(self,l):
        for i in range(0,l):
            v = self.story[i]
            if(v == ' '):
                print('')
            else:
                print(v,end='')
a = string()
a.story = input('Enter the story :')
l = len(a.story)
a.length_word(l)