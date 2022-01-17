def series(a,r,n):
    ans = (a*(r**(n)-1))/(r-1)
    return ans

a = int(input('Enter the first term of G.P series :'))
r = int(input('Enter the r of G.P series :'))
n = int(input('Enter the nth term of G.P series :'))
ans = series(a,r,n)
print(ans)