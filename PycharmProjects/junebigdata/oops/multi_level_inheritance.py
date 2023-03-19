#class a
#class b(a)
#class c(b)

class a:
    def printa(self,num):
        self.num=num
        print("inside class a")
class b(a):
    def printb(self,num1):
        self.num1=num1
        print("inside class b")
class c(b):
    def printc(self,num2):
        self.num2=num2

    def printd(self):
        print(self.num,self.num1,self.num2)

