dic={'id':101,'fname':'vinay','lname':'k','age':25,'prof':'bigdata,','salary':150000}
#key:id,fname,lname,age,prof,salary
#value--->vinay
#corresponding key to fetch values
print(dic['fname'])
print(dic['age'])
for i in dic:
    print(i,',',dic[i])
#how to update a value
#id===>110
dic['id']=110
print(dic['id'])
#Dictionary is mutable
dic['fname']='vimal'
print(dic['fname'])
dic['salary']+=1500 #updating old values
print(dic['salary'])
#ADDING NEW KEY VALUE PAIR
dic['marks']=45
print(dic['marks'])

#CHECKING WHETHER KEY IS PRESENT OR NOT
print('age' in dic)
print('subject' in dic)
print('lname' not in dic)
print('marks' not in dic)

#DELETING A KEY VALUE PAIR
del dic['salary']
del dic['prof']
print(dic)