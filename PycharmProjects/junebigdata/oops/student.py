class student:
    coll='abc'
    def setvalue(self,roll_no,fname,lname,age,department,college):
        self.roll_no=roll_no
        self.fname=fname
        self.lname=lname
        self.age=age
        self.department=department

    def printvalue(self):
        print(self.roll_no,self.fname,self.lname,self.age,self.department,student.coll)

pe1=student()
pe1.setvalue(11,'vinay','k',26,'python','abc')
pe1.printvalue()
print('*'*100)

#2 variable
#1. Instance variable
#2. static variables

