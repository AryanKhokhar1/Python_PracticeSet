class common:
    def make_list(self):
        l = len(self.story)
        s = ''
        lis = list()
        for i in range(0,l):
            v = self.story[i]
            s = s + v
            if(v == ' ' or i == (l - 1)):
                if(i == (l-1)):
                    s = s + ' '
                lis. append(s)
                s = ''
        return lis
    def check(self,lis1,lis2):
        lis = list()
        l = len(lis1)
        for i in range(0,l):
            v = lis1[i]
            if(v not in lis2):
                lis.append(v)
        return lis
    @staticmethod
    def show(res1,res2):
        res = res1 + res2
        l = len(res)
        print('Uncommon word = ',end='')
        for i in range(0,l):
            if(i != (l-1)):
                print(res[i],end=',')
            else:
                print(res[i])
a = common()
b = common()
a.story = input('Enter the first string :')
b.story = input('Enter the second string :')
lisa = a.make_list()
lisb = b.make_list()
res1 = a.check(lisa,lisb)
res2 = b.check(lisb,lisa)
a.show(res1,res2)