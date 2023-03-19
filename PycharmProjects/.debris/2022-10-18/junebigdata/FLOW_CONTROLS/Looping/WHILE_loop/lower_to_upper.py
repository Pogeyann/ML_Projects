lower_limit=int(input('enter lower limit'))
upper_limit=int(input('enter upper limit'))
while(lower_limit<=upper_limit):
    if(lower_limit%2==0):
        print(lower_limit)
    lower_limit+=1 # always put into while loop not in if