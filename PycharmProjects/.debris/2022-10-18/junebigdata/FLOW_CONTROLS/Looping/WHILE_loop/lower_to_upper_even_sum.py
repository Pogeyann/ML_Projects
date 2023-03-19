lower=int(input('enter lower num'))
upper=int(input('enter upper num'))
sum=0
while(lower<=upper):
    if(lower%2==0):
        sum+=lower
    lower+=1
print(sum)