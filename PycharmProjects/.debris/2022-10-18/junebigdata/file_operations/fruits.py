f=open('fruits','r')
f1=open('fruits1','w')
ls=[]
for i in f:
    if i!='apple':
        ls.append(i)