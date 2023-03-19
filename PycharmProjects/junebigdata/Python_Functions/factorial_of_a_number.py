#Factorial
#3methods

# def fact():
#    num=int(input("ent num"))
#    i=1
#    sum=1
#    while(i<=num):
#        sum*=i
#        i+=1
#    print(sum)
#
# fact()

# def fact2(num1):
#     sum=1
#     for i in range(1,num1+1):
#         sum*=i
#     print(sum)
#
# fact2(10)

def fact3(num1):
    i=1
    sum=1
    while(i<=num1):
        sum*=i
        i+=1
    return sum

data=fact3(10)
print(data)