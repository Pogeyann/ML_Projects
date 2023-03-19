#List slicing
lst=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
#index
print(lst[1:5])
print(lst[3:9])
print(lst[6:10])
print(lst[1:]) #index 1 to end of list
print(lst[3:]) #index = 3 to end of list
print(lst[:7]) #index=0 to 6(upper=1)
print(lst[:]) #full list
print(lst[1:8:2]) #similar to for loop #index =1,3,5,7
print(lst[3:14:3]) #index=3,6,9,12
print(lst[3::2]) #index=3,5,7,9,11,13
print(lst[:9:3]) #index=0,3,6
print(lst[::4]) #index=0,4,8,12
