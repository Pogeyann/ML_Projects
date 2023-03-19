#MULTIPLE INHERITANCE
#parent class 1
class person:
    def person_info(self,name,age):
        print("inside person class")
        print('name:',name,"age:",age)
#parent class 2
class company:
    def company_info(self,company_name,location):
        print("inside company class")
        print('name:',company_name,'location:',location)
#child class
class employee(person,company):
    def employee_info(self,salary,skill):
        print('inside employee class')
        print('salary:',salary,'skill:',skill)
emp=employee()
emp.person_info('jessa',28)
emp.company_info('google','atlanta')
emp.employee_info(120000,'machine learning')