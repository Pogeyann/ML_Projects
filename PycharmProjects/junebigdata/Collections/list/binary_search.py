#Binary search
#Algorithm
#step 1
#sort the given array or list (ascending order)
#lst=[15,20,5,8,25,21,16,19,30,28]
#lst=[5,8,15,16,19,20,21,25,28,30] lst.sort()
# low                             upp
#step 2 ; 2 variables
#low =0
#upper=len(lst)-1 #9

#step 3: calculate mid
#mid = (lower + upper)//2   mid=(0+9)//2=4

#step 4 :
# A .search element > lst[mid]    20.>19

#low=mid+1
#B. search element <lst[mid]
# 15<19
#upper=mid-1
#C search element==lst[mid]
 # element found
lst=[5,9,2,15,14,10,7,3,1,13,8]
element=int(input('enter your number'))
lst.sort()
print(lst)
low=0
upp=len(lst)-1 #10
flag=0
while(low<=upp):#0<=10 6<=10 9<=10
    mid=(low+upp)//2 #mid=0+10/2=5,6+10//2=8,9+10//2=9
    if element>lst[mid] #14>8 14>13
        low=mid+1 #5+1=6 8+1=9
    elif element<lst[mid]: #14<14
        upp=mid-1
    elif element==lst[mid]:
        flag=1
        break
if(flag>0):
    print(number)
else:
    print('no number')
    