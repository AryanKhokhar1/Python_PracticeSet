# check given string is pangram or not
def pangram(sentence):
    sentence = sentence.lower()
    lis = 'abcdefghijklmnopqrstuvwxyz'
    r = 0
    for character in lis:
        if(character not in sentence):
            r = 1
    if(r == 0):
        print('This is a pangram sentence')
    else:
        print('This is not a pangram sentence')
sentence = input('Enter a sentence: ')
pangram(sentence)