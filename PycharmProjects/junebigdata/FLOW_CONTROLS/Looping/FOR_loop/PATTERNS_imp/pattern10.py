#0
#01
#024
#0369
#0481216
#0510152025
for i in range(0,6):#0 1 2
    for j in range(0,i+1):#(0,1) j=0 (0,2)0,1 (0,3) 0 1 2(0,4)0 1 2 3
        print(i*j,end=" ")#0 0 1 
    print()

for i in range(0,6):
    for j in range(0,i+1):
        print(i*j,end=" ")
    