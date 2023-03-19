#WORDCOUNT PROBLEM
data='hai hello bigdata python python bigdata hai hai hello hello hai bigdata'
#hai,4
#hello,3
#bigdata,3
#python,2

#wordcount
#split
data1=data.split(" ")
print(data1)
d= {}
#dic={}
#['hai','hello',
#hai,1
#hello,1
#bigdata,2
#python
flag=0
for i in data1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)