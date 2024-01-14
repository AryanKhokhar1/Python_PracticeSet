def duplicate(story,new_list,n):
    if(n == len(story)-1):
        return new_list
    else:
        if(story.count(story[n]) > 1):
            new_list.append(story[n])
    return duplicate(story,new_list,n+1)
story = input('Enter a string: ')
new_list = []
n = 0
ans = duplicate(story,new_list,n)
ans = set(ans)
print('The duplicate characters =',end = ' ')
for i in ans:
    print(i,end='')