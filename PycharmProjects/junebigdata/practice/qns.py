str1="sky is blue"
mylist=str1.split()
mylist=mylist[::-1]
str2=" ".join(mylist)
print(str2)

my_list = list([5, 8, 'Tom', 7.50])

# Using extend()
my_list.extend([25, 75, 100])
print(my_list)