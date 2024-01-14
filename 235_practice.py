from sys import set_coroutine_origin_tracking_depth


def changed(sentence):
    lis_word = list(sentence)
    c = lis_word[0]
    lis_word[0] = lis_word[-1]
    lis_word[-1] = c
    new_word = ''
    for i in range(0,len(lis_word)):
        new_word = new_word + lis_word[i]
    return new_word
sentence = input('Enter a Sentence: ')
ans = changed(sentence)
print('The changed Sentence = ',ans)