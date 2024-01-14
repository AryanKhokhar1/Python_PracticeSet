story = input('Enter the string: ')
sub_story = input('Enter a substring: ')
# rep_story = input('Enter a substring: ')
if(sub_story in story):
    post = story.find(sub_story)
    l = len(sub_story)
    last = post + l
    lis_story = list(story)
    for i in range(post,last):
        lis_story.pop(i)
    print(lis_story)
else:
    print('Given Sub string is not present in the String')