lst=[3,2,1,5,6,4]
#console one elements
#pair
#6
#2,4
#1,5
element=int(input('enter a number')) #6

lst.sort()
print(lst)
low=0
upp=len(lst)-1 #5
while(low<=upp): #0<=5 0<=4
    data=lst[low]+lst[upp] #data=1+6=7 data=1+5=6
    if(data==element):#7==6 6==6
        print('pairs are',lst[low],lst[upp]) #1,5
        break
    elif(data>element):#7>6
        upp=upp-1#4
    else:
        low=low+1