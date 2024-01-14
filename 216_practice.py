import string
from tabnanny import check
class strings:
    def check(self,l,val):
        for n in range(0,l):
            v = self.story[n]
            if(v in string.ascii_letters):
                val = val
            elif(v in '0123456789'):
                val = val
            else:
                val = val + 1
        if(val == 0):
            print('This String does not contain special letter')
        else:
            print('This String contain special Letter')
a = strings()
a.story = input('Enter the String :') 
l = len(a.story)
n = 0
val = 0
a.check(l,val)