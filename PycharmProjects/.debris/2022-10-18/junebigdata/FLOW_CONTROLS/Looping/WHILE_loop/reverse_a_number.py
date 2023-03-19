#Reverse a number
num=int(input('enter a number'))
#153
#153%10=3
#153//10=15
#15%10=5
#15//10=1
#1%10=1
res=0
while(num!=0): #153!=0 15 1!=0
    digit=num%10 #digit=3 15%10=5
    res=(res*10)+digit #res=(8*10)+3=3
    num//=10 #153//10=15 15//10=1
    print(res)