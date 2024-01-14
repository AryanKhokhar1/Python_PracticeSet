class rotate:
    def left_to_right(self):
        print(self.story)
    def right_to_left(self):
        print(self.story[::-1])
    def up_to_down(self):
        l = len(self.story)
        for i in range(0,l):
            print(self.story[i])
    def down_to_up(self):
        l = len(self.story) - 1
        for i in range(l,-1,-1):
            print(self.story[i])

a = rotate()

a.story = input('Enter the String :')
c = input('Enter the the rotation (LTR),(RTL),(UTD) or (DTU)')
if(c == 'ltr' or c == 'LTR'):
    a.left_to_right()
elif(c == 'rtl' or c == 'RTL'):
    a.right_to_left()
elif(c == 'utd' or c == 'UTD'):
    a.up_to_down()
elif(c == 'dtu' or c == 'DTU'):
    a.down_to_up()
else:
    print('You type something wrong')
    