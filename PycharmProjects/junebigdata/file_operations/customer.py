f=open('/home/mush/Downloads/customer','r')
d={}
a=0
ls=[]
for i in f:
    data=i.rstrip("\n").split(",")
    for i in data:#range(len(data))
          if int(data[3])>a:
            a=int(data[3])
            c=data[1:5]
print(c)
    #print(data)

#age mxm 1 employeee fname,lname,age,prof

#Each profession count
#     prof=data[4]
#     for i in data:
#         if prof in d:
#             d[prof]+=1
#         else:
#             d[prof]=1
# for k,v in d.items():
#     print(k,",",v)

#age above 50 and work location us
    # for i in data:
    #     if data[3]>'50' and data[-1]=='us':
    #         print(data[1:5])
#Doctor prof and loc india
#fname,lname,age
    # for i in data:
    #     if data[4]=='Doctor' and data[-1]=='india':
    #         print(data[1:4])
    #         break
#Doctor prof fname,age,country
    # for i in data:
    #      if data[-2]=='Doctor':
    #          print(data[1:6:2])
#india fname,lname,age,prof
    # for i in data:
    #     if data[-1]=='india':
    #         print(data[1:6])

#age above 58 fname,lname,age,prof
    # for i in data:
    #     if data[3]>'50':
            # print(data[1:5])
