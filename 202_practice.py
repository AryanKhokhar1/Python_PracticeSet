class list:

    def append(self,num):
        return self.lis.append(num)
    def delete(self,num):
        return self.lis.remove(num)
    def printing(self):
        print(self.lis)
a = list()
a.lis = [1,3,4]
a.delete(3)
a.append(2)
a.printing()