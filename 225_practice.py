from itertools import permutations
class permutation:
    def display(self):
        lis = list(permutations(self.word))
        l = len(lis)
        for i in range(0,l):
            t = lis[i]
            b = len(t)
            for a in range(0,b):
                print(t[a],end='')
            print('\n')
a = permutation()
a.word = input('Enter the set of words :')
a.display()