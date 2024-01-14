class url:
    def check(self):
        if('www' in self.story):
            l = len(self.story)
            v = self.story
            p = v.find('www')
            print('URL = ',end='')
            for i in range(p,l):
                print(v[i],end='')
                if(v[i] == '.'):
                    if(v[i+1] == 'c'):
                        if(v[i+2] == 'o'):
                            if(v[i+3] == 'm'):
                                print('com')
                                break
        else:
            print('This String does not contain URL')
a = url()
a.story = input('Enter the String :')
a.check()