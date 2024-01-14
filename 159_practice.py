def reverse(s,n,mult):
    mult = mult + s[n]
    if(n == 0):
        return mult
    else:
        return reverse(s,n-1,mult)
story = input('Enter the String here :')
l = len(story) - 1
mult = ''
ans = reverse(story,l,mult)
print(f'Reversed order of {story} = {ans}')