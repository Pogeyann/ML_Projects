f=open('fruits','r')
f1=open('fruits1','w')
ls=[]
for i in f:
    data=i.rstrip("\n")
    ls.append(data)

for i in data:
    if i!= 'apple':
        data.write(i)
