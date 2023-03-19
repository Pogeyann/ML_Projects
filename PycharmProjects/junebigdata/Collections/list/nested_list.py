#NESTED list
lst=[[101,'vinay','k',26,'ppython',1000],
     [102,'amal','p',25,'bigdata',1500],
     [103,'vineeth','t',27,'python',2000],
     [104,'vimal','k',26,'bigdata',1750],
     [105,'anoop','r',28,'python',2000]]
#print(lst
sum=0
for i in lst:
    sum+=i[5]
print(sum)