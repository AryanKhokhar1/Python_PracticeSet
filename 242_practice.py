# count lowercase letter
def lowercounter(sentence):
    n = 0
    for character in sentence:
        if(character <= 'z' and character >= 'a'):
            n = n + 1
    return n
sentence = input('Enter the sentence: ')
ans = lowercounter(sentence)
print('The total number of lower case letter =',ans)