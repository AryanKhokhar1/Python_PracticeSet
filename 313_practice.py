story = input('Enter the string: ')
story = story.split(' ')
for i in range(len(story)):
    d = dict(zip(str(i),story[i]))
print(d)