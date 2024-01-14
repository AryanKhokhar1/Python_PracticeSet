def palindrome(story):
    a = story[::-1]
    print(a)
    if(story == a):
        print('This is a Palindrome String')
        return
    else:
        print('This is not a Palindrome String')
        return
story = input('Enter the string (weather a string palindrome or not) :')
palindrome(story)