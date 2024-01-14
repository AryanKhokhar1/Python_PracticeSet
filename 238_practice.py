def length(subject):
    a = 0
    for i in subject:
        a = a + 1
    return a
word = input('Enter the word or sentence: ')
ans = length(word)
print('The length of word or sentence =',ans)