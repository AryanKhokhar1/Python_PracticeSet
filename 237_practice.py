# change space to hyphen
def hyphen_changer(sentence):
    lis_word = list(sentence)
    new_sentence = ''
    for i in range(len(lis_word)):
        if(lis_word[i] == ' '):
            lis_word[i] = '-'
    for i in range(len(lis_word)):
        new_sentence = new_sentence + lis_word[i]
    return new_sentence
sentence = input('Enter a sentence: ')
ans = hyphen_changer(sentence)
print(ans)