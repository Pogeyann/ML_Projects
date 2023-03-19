#1. How to define
#1. How to define

# lst=[] #Using square bracket
#1. print(type(lst))
# 2. lst1=list()
# print(type(lst1))

#2. Heterogeneous is supported or not

lst1=[10,10.5,10.555555555,'bigdata','luminar',True,False]
print(lst1)
# It supports heterogeneous data

#3.Duplicates allowed or not

lst2=[10,10,10,20,20,20,'bigdata','bigdata','bigdata']
#It supports duplicates
print(lst2)


#4. Insertion order is preserved or not
lst=[10,101,102,103,'bigdata',104,105,'python,']
print(lst)

# Insertion order is preserved

#0...............n-1

# corresponding elements has index values
# Index value

print(lst) #
print(lst[3])
print(lst[7])

#list mutable

#40===>75
lst[3]=75
print(lst)