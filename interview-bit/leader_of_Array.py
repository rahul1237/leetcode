A=[16, 17, 4, 3, 5, 2]

n=len(A)
maxi=A[n-1]
ans=[]
ans.append(maxi)

for _ in range(n-1,-1,-1):
    if(A[_]>maxi):
        ans.append(A[_])
        maxi=max(maxi,A[_])

print(ans)