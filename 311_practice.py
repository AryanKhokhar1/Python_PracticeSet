class Dictionary:
    def make_list1(self,n):
        lis = []
        for i in range(n):
            a = int(input(f'Enter the {i+1} element for list: '))
            lis.append(a)
        return lis
    def make_list2(self,n):
        lis = []
        for i in range(n):
            a = int(input(f'Enter the {i+1} element for list: '))
            lis.append(a)
        return lis
a = Dictionary()
n = int(input('Enter the number of term: '))
ans1 = a.make_list1(n)
ans2 = a.make_list2(n)
print(dict(zip(ans1,ans2)))