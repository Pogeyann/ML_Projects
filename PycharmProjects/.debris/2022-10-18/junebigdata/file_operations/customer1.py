f=open('/home/mush/Downloads/customer','r')
d={}
for i in f:
    data=i.rstrip("\n").split(",")
