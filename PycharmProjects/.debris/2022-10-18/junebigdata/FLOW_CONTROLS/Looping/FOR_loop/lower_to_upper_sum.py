lower=int(input('enter lower'))
upper=int(input('enter upper'))
sum=0
sum1=0
for i in range(lower,upper+1):
    if(i%2==0):
        sum+=i
    else:
        sum1+=i
print(sum)
print(sum1)