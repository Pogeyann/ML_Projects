#Using function to create a calculator
#1.Addition
#2.substraction
#3.Multiplication
#4.Division

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return (num1*num2)
def div(num1,num2):
    return (num1/num2)
print("1.Addition\n"
      "2.Substraction\n"
      "3.multiplication\n"
      "4.Division\n")
num1=int(input("enter number1"))
num2=int(input("enter number2"))
choice=int(input("enter your choice 1/2/3/4"))
if choice==1:
    print(num1,"+",num2,add(num1,num2))
elif choice==2:
    print(num1,"-",num2,sub(num1,num2))
elif choice==3:
    print(num1,"*",num2,mul(num1,num2))
elif choice==4:
    print(num1,"/",num2,div(num1,num2))