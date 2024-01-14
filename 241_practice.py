def show(a,b):
    ca = 0
    cb = 0
    for word1 in a:
        ca = ca + 1
    for word2 in b:
        cb = cb + 1
    if(ca > cb):
        print(a)
    elif(cb>ca):
        print(b)
    else:
        print('Both have equal character')
story1 = input('Enter 1st sentence: ')
story2 = input('Enter 2nd sentence: ')
show(story1,story2)