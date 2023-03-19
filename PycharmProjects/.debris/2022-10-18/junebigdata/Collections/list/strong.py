#for i in range
#for i in lst
#for i in 'luminar'
#if i in lst:   i==
#if i not in lst

lst=[10,20,30,40,50]
print(100 in lst)

lst1=[10,20,10,20,30,30,40,50,50,40]
lst2=[]

for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)