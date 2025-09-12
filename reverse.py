#  Reverse a string without using slicing.

str = "Priyanka"

for i in range(len(str),0,-1):
    print(str[i-1], end='')
