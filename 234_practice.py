def angrom_check(word1,word2):
    if(len(word1) == len(word2) and ' ' not in word1 and ' ' not in word2):
        lis_word = list(word1)
        r = 0
        for character in lis_word:
            if(word1.count(character) == word2.count(character)):
                pass
            else:
                r = 1
        if(r == 0):
            print("It's a Anagram Number")
        elif(r == 1):
            print("It's not a Anagram Number")
    else:
        print("It's not a Anagram Number")
word1 = input('Enter 1st word: ')
word2 = input('Enter 2nd word: ')
angrom_check(word1,word2)