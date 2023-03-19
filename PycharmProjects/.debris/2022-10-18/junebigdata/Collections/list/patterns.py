#interview qn
lst=[6,5,8,12,18,20,25]
#lst1=[88,89,86,82,76,74,69]
#lst2=[5,10,25,40,30]
#lst3=[105,100,85,70,80]
lst1=[]
sum1=sum(lst) #94
print(sum1)
for i in lst: #6
    res=sum1-i#res=94-6=88
    lst1.append(res)
print(lst1)