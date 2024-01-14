# count number of digits and letters
def counter(sentence):
    nl = 0
    nd = 0
    for character in sentence:
        if(character in '0123456789'):
            nd = nd + 1
        elif(character <= 'z' and character >= 'A'):
            nl = nl + 1
    print('Total number of digit in sentence =',nd)
    print('Total number of letter in sentence =',nl)
sentence = input('Enter a sentence: ')
counter(sentence)