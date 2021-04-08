A="ivjwvi"

a=len(A)-1
b=0
ans=0
while(b<=a):
    if(ans>1):
        print(0)
    if(A[b]!=A[a]):
        ans+=1
        b+=1
        continue
    a-=1
    b+=1
print(1)