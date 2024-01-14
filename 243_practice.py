def palindrome(word):
    if(word == word[::-1]):
        print("It's a palindrome string")
    else:
        print("It's not a palindrome string")

word = input('Enter a word: ')
palindrome(word)