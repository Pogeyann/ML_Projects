#multiple inheritance
#more than one parent class
class a:
    def printa(self,num):
        self.num=num
        print('inside class a',self.num)

class b:
    def printb(self,num1):
        self.num1=num1
        print("inside class b",self.num1)

class c(b,a):
    def printc(self,num2):
        self.num2=num2
        print("inside class c ",self.num2)

c1=c()
c1.printc(5)
c1.printa(4)
c1.printb(50)