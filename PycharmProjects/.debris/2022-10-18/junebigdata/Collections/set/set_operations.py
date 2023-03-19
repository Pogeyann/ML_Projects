#SET OPERATIONS

#3 TYPES OF OPERATIONS
# 1.UNIOn_OPERATIONS
# 2.INTERSECTION_OPERATIONS
# 3.DIFFERENCE_OPERATIONS

st1={1,2,3,4,5,6,7,8,9,10}
st2={5,6,7,8,9,10,11,12,13,14,15}
#UNION
#COMBINED RESULT
st3=st1.union(st2) #{1,2,3,4,5,....15}
print(st3)
#Intersection
#COMMON result
st4=st1.intersection(st2)
print(st4)
#DIFFERENCE OPERATION
#A-B=ELEMENT PRESENT IN A NOT IN B
#st1-st2=={1,2,3,4}
st3=st1.difference(st2)
print(st3)
st3=st2.difference(st1)
print(st3)