def new_word(s):
    return s[0]+s[1]+s[-2]+s[-1]
string = input('Enter string: ')
ans = new_word(string)
print('New string =',ans)