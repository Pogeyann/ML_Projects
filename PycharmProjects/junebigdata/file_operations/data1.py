f=open('/home/mush/PycharmProjects/junebigdata/file_operations/data1','r')
f1=open('write_data1','w')
for i in f:
    f1.write(i)