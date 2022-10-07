
#recursion logic
#1 identify base case
#2 identify how problem can be solved using solution of sub problem
#3 apply the relation

# Identify the number of possible paths
# [
#     [0,-,-,-],  have to reach x from o
#     [-,-,-,-],  can only go down or right
#     [-,-,-,-],
#     [-,-,-,x]
# ]

def rec(x,y):
    #base case
    if(x==1 or y==1):
        return(1)
    else:
        return(rec(x-1,y)+rec(x,y-1))


print(rec(3,4))