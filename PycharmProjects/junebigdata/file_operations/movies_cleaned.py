f=open('/home/mush/Downloads/movies_cleaned1.csv','r')
lst=[]
g=0
for i in f:
    data=i.rstrip("\n").split(",")
    #print(data)
#1.2010 movies name,rating,year,duration
#2.Each year release movie count
#3.rating above 4 movies name,rating,year
#4.year 2005 and rating above 4 name,year,rating
#5.rating mxm movies full data
    rate=float(data[3])
    if rate>g:
        g=rate
        lst.append(data)
#print(lst"*"*100)
for i in lst:
    rate=float(i[-2])
    if rate==g:
        print(i)


