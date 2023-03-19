#id,fname,lname,age,salary
dic={'id':1,'fname':'sabir','lname':'m','age':31,'salary':80000}
#age update
dic['age']=33
print(dic['age'])
#company:luminartechnolab
print('company' in dic)
dic['company']='luminartechnolab'
#employee fname
print(dic['fname'])
del dic['lname']
#salary 1000 add
dic['salary']+=1000
#key-value print
for i in dic:
    print(i,dic[i])