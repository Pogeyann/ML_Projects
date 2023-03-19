#console 3 nos
#nested if else
#second largest number
num1=int(input('enter num1'))
num2=int(input('enter num2'))
num3=int(input('enter num3'))

if(num1>num2)&(num1>num3):
    if(num2>num3):
       print('2nd largest no is', num2)
    else:
        print('2nd largest no is', num3)
elif(num2>num3)&(num2>num1):
    if(num3>num1):
       print('2nd largest no is', num3)
    else:
        print('2nd largest no is',num1)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print('2nd largest no is',num1)
    else:
        print('2nd largest no is',num2)
else:
    print('failed')