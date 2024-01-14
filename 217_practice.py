import random
import string
class strings:
    def rand_string(self,lis):
        if(self.story == '' ):
            for i in string.ascii_letters:
                lis.append(i)
            for a in range(0,5):
                n = random.randint(1,9)
                for i in range(0,n):
                    v = random.choice(lis)
                    print(v,end='')
                    if(i == (n-1)):
                        print(end=' ')
        print(self.story)
a = strings()
a.story = input('Enter the story :')
lis = list()
a.rand_string(lis)