from functools import reduce


def deletion(story):
    if(len(story) == 0):
        return story
    else:
        story.pop()
        print()
        for word in story:
            print(word,end='')
        return deletion(story)
story = input('Enter a string: ')
story = list(story)
deletion(story)