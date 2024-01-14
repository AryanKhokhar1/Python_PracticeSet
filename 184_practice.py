def letter(story,l):
    return story.count(l)
story = input('Enter the story :')
l = input('Enter the letter :')
ans = letter(story,l)
print(ans)