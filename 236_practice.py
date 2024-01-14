def vowel_counter(sentence):
    a = 0
    for word in sentence:
        if(word in "aeiouAEIOU"):
            a = a + 1
    return a
sentence = input('Enter a sentence: ')
ans = vowel_counter(sentence)
print("Number of vowels =",ans)