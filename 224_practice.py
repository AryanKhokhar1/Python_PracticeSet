# 224.	 Python – Replace multiple words with K

class duplicate:
    @staticmethod
    def count(lis,val):
        a = 0
        l = len(lis)
        for i in range (0,l):
            if(val == lis[i]):
                a = a + 1
        return a
    def make_list(self):
        s = ''
        lis = list()
        l = len(self.story)
        # a.display()
        for i in range(0,l):
            v = self.story[i]
            if(v == ' ' or i == (l-1)):
                if(i == (l-1)):
                    s = s + v
                lis.append(s)
                s = ''
            else:
                s = s + v
        return lis
    def check_duplicate(self,lis):
        l = len(lis)
        for i in range(0,l):
            v = lis[i]
            ans = a.count(lis,v)
            if(ans > 1):
                for va in range(0,l):
                    if(v == lis[va]):
                        lis[va] = 'K'
        return lis
    def display(self,lis):
        l = len(lis)
        for i in range(0,l):
            print(lis[i],end=' ')
a = duplicate()
a.story = input('Enter the Story :')
ans = a.make_list()
lis = a.check_duplicate(ans)
a.display(lis)