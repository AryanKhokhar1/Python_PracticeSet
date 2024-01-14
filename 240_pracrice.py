# count word and character
def counter(sentence):
    lis_word = sentence.split(' ')
    print('The total number of words =',len(lis_word))
    lis_character = list(sentence)
    for i in range(len(lis_character)):
        if(lis_character[i] == ' '):
            lis_character[i] = ''
    word = ''
    for i in range(len(lis_character)):
        word = word + lis_character[i]
    print('The total number of character =',len(word))
sentence = input('Enter the sentence: ')
counter(sentence)