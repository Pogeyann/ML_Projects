class person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class employee(person):
    company_name='ABC'
    def setvalue(self,id,dept,salary):
        self.id=id
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print(self.name,self.age,self.place,self.id,self.dept,self.salary,employee.company_name)

em1=person()
em1.setvalue('mushthaq',27,'vaduthala',1,'data_science',120000)
em1.printvalue()