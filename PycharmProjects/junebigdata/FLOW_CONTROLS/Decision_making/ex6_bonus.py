salary=int(input("enter salary"))
exp=int(input("enter years of experience"))
bonus=salary*0.05
if(exp>5):
    print('achieved bonus',bonus)
else:
    print('no bonus')