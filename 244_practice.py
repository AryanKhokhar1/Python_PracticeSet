# count lowercase letter
def lowercounter(sentence):
    nl = 0
    nu = 0
    for character in sentence:
        if(character <= 'z' and character >= 'a'):
            nl = nl + 1
        elif(character <='Z' and character >= 'A'):
            nu = nu + 1
    return nl,nu
sentence = input('Enter the sentence: ')
ans = lowercounter(sentence)
print('The total number of lower case letter =',ans[0])
print('The total number of Upper case letter =',ans[-1])