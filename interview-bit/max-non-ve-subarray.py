A=[1,2,5,-7,2,3]

sum=0
maxsum=0
left=0
right=0
al=-1
ar=-1
ans=[]

for _ in range(len(A)):
    if(A[_]>=0):
        sum+=A[_]
        if(sum>maxsum or (sum==maxsum and ar-al < right-left)):
            maxsum=sum

            al=left
            ar=right
    else:
        sum=0
        left=_+1
    right+=1


if(al==-1):
    print(ans)

for _ in range(al,ar+1):
    ans.append(A[_])
print(ans)