class check:
    def palindrome(self):
        r = self.story[::-1]
        if(self.story == r):
            print("It's a Palindrome Number ")
        else:
            print("It's not a Palindrome Number ")
a = check()
a.story = input('Enter the string for check palindrome condition :')
a.palindrome()