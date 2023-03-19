#check given number is prime number or not
#2,3,5,7,11,13,17,19,23
#9(1,3,9)
#12(1,2,4,6,12)
#15(1,3,5,15)

#9 [2,.....8]
#99%2==0
#9%3==0
#9%4==0
flag=0
num=int(input('enter num'))
for i in range(2,num):
    if(num%i==0):
      flag=1
    break#(modified)

if(flag>0):
    print('number is not a prime')
else:
    print('number is prime')
    #     print('not a prime number')
    # else:
    #     print('prime number')