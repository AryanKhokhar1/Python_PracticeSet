class binary:
    def check(self):
        l = len(self.start)
        a = 0
        for i in range(0,l):
            v = self.start[i]
            if(v != '0' and v != '1'):
                print('Given String is not binary string')
                a = 1
                break
        if(a == 0):
            print('Given String is a binary string')
a = binary()
a.start = input('Enter a number for binary string condition check :')
a.check()