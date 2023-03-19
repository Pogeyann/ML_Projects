f=open('/home/mush/Downloads/patent','r')
d={}
for i in f:
    data=i.rstrip("\n").split(" ")
    # print(data)
#FINDING COUNT
    d={}
    pat=data[0]
    subpat=data[1]
    for i in data:
        if pat not in d:
            d[pat]=1
        else:
            d[pat]+=1
            for k,v in d.items():
                print(k,",",v)
#print(d)
#FOR FINDING HIGHER VALUE
    # pat=data[0]
#     #d[pat]=1
#     sub_patent=float(data[1])
#     if pat not in d:
#         d[pat]=sub_patent
#     else:
#         old=d[pat]
#         if sub_patent>old:
#             d[pat]=sub_patent
# print(d)