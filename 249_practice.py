def occurence(sentence):
    set_sentence = set(sentence)
    lis_sentence = list(set_sentence)
    for character in lis_sentence:
        if(character != ' '):
            print(f'Counting of {character} in sentence =',sentence.count(character))
sentence = input('Enter a sentence: ')
occurence(sentence)