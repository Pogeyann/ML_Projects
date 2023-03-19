#read lower and upper from console and print only even nos
lower_limit=int(input('enter lower limit'))
upper_limit=int(input('enter upper limit'))
i=lower_limit%2==0
while(i<=upper_limit):
    print(i)
    i+=1