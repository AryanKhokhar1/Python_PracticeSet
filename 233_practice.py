def deletion(story,n):
    story = list(story)
    story.pop(n-1)
    for word in story:
        print(word,end='')
story = input('Enter a String: ')
n = int(input('Enter the nth term of string: '))
if(n < len(story)):
    deletion(story,n)
else:
    print('The given indexed is not exist in the string')