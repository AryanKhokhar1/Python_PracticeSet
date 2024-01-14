def reverse(story,l):
    print(story[l],end='')
    if(l == 0):
        return
    else:
        return reverse(story,l-1)
story = input('Enter the string :')
l = len(story) -1
reverse(story,l)