def display(lis):
    c = lis[0]
    lis[0] = lis[-1]
    lis[-1] = c
    print(lis)
lis = [1,2,3,4,5,6,7,8,9]
display(lis)