#Tuples
#properties
#1.How to define
# ()-parenthesis
# tu=()
# print(type(tu))
# #tuple function
# tu1=tuple()
# print(type(tu1))
#2.Heterogeneous or not 3.duplication
tu1 =(10,10.5,'bigdata','bigdata','bigdata',True,False,10.5555)#it supports duplication
# and heterogeneous
print(tu1)
#4.Insertion order is preserved
#mutable
tu2=(10,15,20,25,50,60,70,100)
#15==>75
tu2[1]=75
#tuple is immutable