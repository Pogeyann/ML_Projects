#Logical Operators
#1. AND &
#2. OR |
#3. XOR ^

# AND OPERATOR
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1
num1=4
num2=3
print(num1&num2)
#num1 4 0 1 0 0
#num2 3 0 0 1 1
#AND    0 0 0 0 (0)
num1=6
num2=7
print(num1&num2)

#num1 6
#OR OPERATOR
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

num1= 4
print(bin(num1))

#XOR OPERATOR
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0
num1=5
num2=7
print(num1^num2)
# 0 1 0 1
# 0 1 1 1
# 0 0 1 0