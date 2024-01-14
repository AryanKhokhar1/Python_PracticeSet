class check:
    def palindrome(self):
        r = self.story[::-1]
        if(self.story == r):
            print("It's a Palindrome Number ")
        else:
            print("It's not a Palindrome Number ")
    def symmetric(self):
        l = len(self.story)
        if(l % 2 == 0):
            if(self.story[0:(l//2)] == self.story[(l//2):]):
                print("It's a Symmetric String")
            else:
                print("It's not a Symmetric String")
        else:
            if(self.story[0:(l//2)] == self.story[(l//2)+1:]):
                print("It's a Symmetric String")
            else:
                print("It's not a Symmetric String")
a = check()
a.story = input('Enter the string for check palindrome condition :')
a.palindrome()
a.symmetric()