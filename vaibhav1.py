n,k=input().split(" ")
n=int( n)
k=int(k)

l=input().split(" ")
l=[int(i) for i in l]
l=sorted(l)
ans=[]
if n==0:
    ans.append(abs(l[0]-l[-1]))
elif n==1:
    ans.append(abs(l[0]-l[-1]))
    ans.append(abs(abs(l[0]-l[-1])-k))
elif n>=2:
    ans.append(abs(l[0]-l[-1]))
    ans.append(abs(abs(l[0]-l[-1])-k))
    ans.append(abs(abs(l[0]-l[-1])-(2*k)))

print(min(ans))