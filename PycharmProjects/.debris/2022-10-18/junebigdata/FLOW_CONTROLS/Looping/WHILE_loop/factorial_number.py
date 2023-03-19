#factorial
fact=int(input('enter number'))
i=1
sum=1
while(i<=fact):#1 2 3
    sum*=i #1*1=1 1*2=2,2*3=6
    i+=1 #1+1=2,2+1=3
print(sum)
