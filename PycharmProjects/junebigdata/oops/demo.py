#id,fname,lname,age,dept,salary,company_name
class employee:
    company_name='luminar'
    def setvalue(self,id,fname,lname,age,dept,salary):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print(self.id)
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.dept)
        print(self.salary)
        print(employee.company_name)

em1=employee()
em1.setvalue(101,'vimal','k',25,'testing',15000)
em1.printvalue()
em2=employee()
em2.setvalue(102,'vinay','m',28,'bigdata',20000)
em2.printvalue()