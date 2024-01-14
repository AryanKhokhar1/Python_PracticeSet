class Check:
    def string(self,s):
        if(s in self.story):
            print("Yess! It's present in the story")
        else:
            print('Nope! It\'s not present in the story')
a = Check()
a.story = 'Hlw My name is Aaryan Khokhar'
small_str = input('Enter the string :')
a.string(small_str)