
n=5
temp_rev=''
temp_fwd=''
temp_drev=''
temp_dfwd=''
# print(str)
for i in range(1,n+1):
    temp_fwd= temp_fwd+str(i)
    if i!=1:
        temp_rev= str(i)+temp_rev
    # print(temp_fwd)
    print((n-i)*' '+temp_rev+temp_fwd)

for i in range(1,n):
    temp_drev=temp_rev[i:n]
    temp_dfwd= temp_fwd[0:n-i]
    print((i-1)*' ',temp_drev+temp_dfwd)










# Output:

#     1
#   212
#   32123
#  4321234
# 543212345
#  4321234
#   32123
#   212
#     1
