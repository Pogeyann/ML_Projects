#person name,age,(personall information)
#parent place,ph (contact information)
#employee id ,designation,salary,company_name
#idname,age,place,designation,salary,company name

class person:
    def printperson(self,name,age):
        self.age=age
        self.name=name


class parent():
    def printparent(self,place,ph):
        self.place=place
        self.ph=ph


class employee(parent,person):
    company_name="abc"
    def printemployee(self,id,designation,salary):
        self.id=id
        self.designation=designation
        self.salary=salary
    def printdata(self):
        print(self.name,self.age,self.place,self.ph,self.id,self.designation,self.salary,employee.company_name)

em1=employee()
em1.printemployee('vinay',25)
em1.printemployee()