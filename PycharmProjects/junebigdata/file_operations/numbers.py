# f=open('number','r')
# lst=[]
# for i in f:
#     lst.append(i)
# print(lst)
# #rstrip
# #lstrip
data='hello\n'
data1=data.rstrip("o\n")
print(data1)
f=open('number','r')
lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))