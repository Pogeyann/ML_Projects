#linear search algorithm
lst=[10,20,30,40,50,60,70,80,89,100]
num=int(input("enter number"))
flag=0
for i in lst:
    if num==i:
        flag=1
        break

if flag>0:
    print(num)
else:
    print("no number")
    #Linear search method
    #drawback:Time complexity is higher
    #Binary search algorithm
