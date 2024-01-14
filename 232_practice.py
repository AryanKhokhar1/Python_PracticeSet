# replace a by $
def changer(story):
    lis_story = list(story)
    for i in range(len(lis_story)):
        if(lis_story[i] == 'a'):
            lis_story[i] = '$'
    return lis_story
story = input('Enter a String: ')
ans = changer(story)
for character in ans:
    print(character,end='')