#1
#2  3
#4  5  6
#7  8  9  10
#11 12 13 14 15
#16 17 18 19 20 21

# 1=1
# 2=3
# 3=6
# 4=10

# 1(1)+0=1
# 2(1)+1=3
# 3(1)+3=6
# 4(1)+6=10
# 5(1)+10=15
# 6(1)+15=21
# 7(1)+21=28
# 8(1)+28=36
# 9(1)+36=45
# 10(1)+45=55
# 11(1)+55=66


def pattern(n):
    if n%2==0:
        return(val(n)-(n/2) + 0.5)*n
    else:
        return(val(n)-(n//2))*n


    

def val(n):
    if n==1:
        return 1
    else:
        return val(n-1)+n

print(pattern(6))

# print(val(5))
for i in range(1,120):
    print(pattern(i))