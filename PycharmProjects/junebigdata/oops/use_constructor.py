#person name,age,place
#student ,roll dept
class person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class student(person):
    def __init__(self,roll,dept,age,name,place):
        super().__init__(name,age,place)
        self.roll=roll
        self.dept=dept
    def printvalue(self):
        print(self.roll,self.name,self.age,self.place,self.dept)
st=student(101,'vinay',26,'eklm','bigdata')
st.printvalue()
