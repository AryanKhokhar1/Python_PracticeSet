# remove odd index value
def odd_index(word):
    lis_word = list(word)
    new_word = ''
    for i in range(0,len(word),2):
        lis_word[i] = ''
    for character in lis_word:
        new_word = new_word + character
    return new_word

word = input('Enter the word: ')
ans = odd_index(word)
print(ans)