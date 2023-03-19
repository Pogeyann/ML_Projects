class person:
    def setvalue(self,name,age,place,phno):
        self.name=name
        self.age=age
        self.place=place
        self.phno=phno
    def printvalue(self):
        print(self.name,self.age,self.place,self.phno)

pe1=person()
pe1.setvalue('vinay',26,'erklm',45678)
pe1.printvalue()
pe2=person()
pe2.setvalue('mush',27,'ekm',9598)
pe2.printvalue()