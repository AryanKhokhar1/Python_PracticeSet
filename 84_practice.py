# n = 1000
# a = 1
# b = 1
# for i in range(1,10):
#     print(f'{i}. {a} + {b} = {a + b}')
#     p = a
#     a = b
#     b = p + b

def call(a ,b):
    print(f'{a} + {b} = {a + b}\n')
    p = a
    a = b
    b = p + b
    if(a >= 8 or b >= 13):
        return 1
    else:
        return call(a,b)
# num = 15
a = 1
b = 1 
l = call(a , b)
# print(l)