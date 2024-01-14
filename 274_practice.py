from ast import Pass
from urllib.parse import ParseResultBytes


lis = [1,3,4,[1,4],[],7,[]]
new_list = []
for i in range(len(lis)):
    if(type(lis[i]) == list):
        if(len(lis[i]) != 0):
            new_list.append(lis[i])
    else:
        new_list.append(lis[i])
print(new_list)