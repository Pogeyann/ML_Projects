f=open('/home/mush/Downloads/temper','r')
#file_read
d={}
for i in f:
    data=i.rstrip("\n").split(",")
    #print(data)
    dist=data[0]
    temp=data[1]
    if(dist not in d):#trivandrum,30  triv,28
        d[dist]=temp #triv=30
    else:
        old=d[dist] #28
        if temp>old:
            d[dist]=temp
print(d)

    #2 columns
    #disrict=data[0]
    #temp=data[1]
    #dis=tem

    #else
    #dis =data[0]
    #tem=data[1]
    #dic[dis]=tem tri,30
    #tri 28

    #else:
    #old=dic[district]

