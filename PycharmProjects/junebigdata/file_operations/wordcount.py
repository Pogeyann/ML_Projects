f=open('wordcount','r')
d={}
for i in f:
    data=i.rstrip("\n").split(" ")
    # print(data)
    for i in data:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            for k,v in d.items():
                print(k,",",v)