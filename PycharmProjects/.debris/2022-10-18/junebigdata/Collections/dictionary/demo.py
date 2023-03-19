#DICTIONARY
#1.HOW TO DEFINE
dic={}
print(type(dic))
#key-value pairs
#id:101
#fname:vinay
#lname:k
#age:25
#prof:bigdata
dic={'id':101,'fname':'vinay','lname':'k','age':25,'prof':'bigdata'}
print(dic)
#heterogeneous supported
#insertion order is preserved
dic={'id':101,'fname':'vinay','age':25,'marks':25,'score':25,'score':30}
print(dic)
#duplicate value supported not keys

#dictionary is mutable
dic['id']=102
print(dic)