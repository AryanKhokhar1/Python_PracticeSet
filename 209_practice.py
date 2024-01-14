class string:
    def length1(self):
        print('Length of Story =',len(self.story))
    def length2(self):
        self.story = list(self.story)
        print('Length of Story =',len(self.story))
    def length3(self):
        self.story = tuple(self.story)
        print('Length of Story =',len(self.story))
    def length4(self):
        counter = 0
        for i in self.story:
            counter += 1
        print('Length of Story =',counter)
a = string()
a.story = input('Enter the Story:')
a.length1()
a.length2()
a.length3()
a.length4()