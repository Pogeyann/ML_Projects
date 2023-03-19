#print even and odd
lower=int(input('enter lower'))
upper=int(input('enter upper'))
even_sum=0
odd_sum=0

while(lower<=upper):
    if(lower%2==0):
        even_sum+=lower #2+4
    else:
        odd_sum+=lower
    lower+=1
print(even_sum)
print(odd_sum)