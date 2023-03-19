#sample.txt
#wordcount
f=open('/home/mush/Downloads/sample.txt','r')
d={}
for i in f:
    data=i.rstrip("\n").split(" ")
    for i in data:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
for k,v in d.items():
    print(k,",",v)