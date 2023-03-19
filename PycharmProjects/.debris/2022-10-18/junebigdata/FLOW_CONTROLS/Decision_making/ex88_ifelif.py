#2nd largest no
num1=int(input('enter num1'))
num2=int(input('enter num2'))
num3=int(input('enter num3'))
if(num3>num1)&(num1>num2)&(num3>num2):
    print('num1 is second largest')
elif(num3>num2)&(num2>num1)&(num3>num1):
    print('num2 is 2nd largest')
elif(num1>num3)&(num3>num2)&(num1>num2):
    print('num3 is 2nd largest')
elif(num2>num1)&(num1>num3)&(num2>num3):
    print('num1 is 2nd largest')
elif(num1>num2)&(num2>num3)&(num1>num3):
    print('num2 is 2nd largest')
elif(num2>num3)&(num3>num1)&(num2>num1):
    print('num3 is 2nd largest')
else:
    print('equal')
