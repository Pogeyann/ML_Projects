num=int(input('enter num'))
a=0
b=1
if num<0:
    print('incorrect input')
elif num==0:
    print(0)
elif num==1:
    print(b)
else:
    for i in range(1,num+1):
        num=a+b
        a=b
        b=num

print(b)