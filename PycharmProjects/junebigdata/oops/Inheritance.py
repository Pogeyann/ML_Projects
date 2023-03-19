#Inheritance
import AptUrl.AptUrl


class A:
    def printa(self,num):
        self.num=num
        print('inside class A',self.num)

class B(A):
    def printb(self,num):
        self.num=num
        print('inside classB',self.num)

a=A()
a.printa(7)
b=B()
b.printb(5)