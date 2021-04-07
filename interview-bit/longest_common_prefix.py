A=["abab", "ab", "abcd"]
A=sorted(A)
if(len(A)<=1):
    print(A[0])

ans=''

for _ in range(len(A[0])):
    for i in range(len(A)):
        if(A[i][_]!=A[0][_]):
            print(ans)
    ans+=A[0][_]

print(ans)