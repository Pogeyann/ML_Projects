tu=(10,15,20,25,30,35,40,45,50,55,60)
#20===>100
#tuple is immutable
lst=list(tu)
print(lst)
lst[2]=100
print(lst)
tu=tuple(lst)
print(tu)