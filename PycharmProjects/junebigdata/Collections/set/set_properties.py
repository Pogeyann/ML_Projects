#properties
#1.How to define
st=set()#empty set created using set function
#normal set can be created using curly bracket

print(type(st))
#2.heterogeneous supported ornot
st1={10,20,30,40,50,'bigdata','python',10.55,True}
print(st1)
#3.Insertion order is not preserved\
#4..duplicate value
st2={10,10,20,30,'bigdata','bigdata',1,True,0,False} #duplicate not supported
print(st2)#heterogeneous supported
#set mutable
st2.add(100)
print(st2)