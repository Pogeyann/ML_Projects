#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

for i in range(1,6):#1,2,3,4,5
    for j in range(1,i+1):#1,12,123,1234,12345
        print(j,end=" ")
    print()