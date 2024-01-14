
import string
story = input('Enter the story(to check pangram condition) :')
l = len(story)
z = 0
for i in string.ascii_letters:
    if(i in story or i.upper() in story):
        z = 1
    else:
        print("It's not a pangram Number ")
        break
if(z == 1):
    print(story,'\n It is a pangram Number')