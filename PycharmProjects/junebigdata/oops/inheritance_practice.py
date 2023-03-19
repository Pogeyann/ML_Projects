class person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number



class employee(person):
    def __init__(self,name,id_number,salary,post):
        self.post=post
        self.salary=salary
        person.__init__(self,name,id_number)
    def display(self):
        print(self.post)
        print(self.salary)
        print(self.name)
        print(self.id_number)


a=employee('rahul',886012,20000,"intern")
a.display()