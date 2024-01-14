n = int(input('Enter a range: '))
a = 1
b = 1
t = 2
print(a,end=',')
print(b,end=',')
for i in range(1,n-1):
    t = t + (a+b)
    print(f'{a + b}',end = ',')
    p = a
    a = b
    b = p + b
print('\nSum =',t)

# def call(a ,b):
#     print(f'{a} + {b} = {a + b}\n')
#     p = a
#     a = b
#     b = p + b
#     if(a >= 8 or b >= 13):
#         return 1
#     else:
#         return call(a,b)
# # num = 15
# a = 1
# b = 1 
# l = call(a , b)
# # print(l)