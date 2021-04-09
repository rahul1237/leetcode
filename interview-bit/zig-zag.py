A,B='abcd',2

if(B==1):
    print(A)

a=2*B-2
ans=[]
for _ in range(B):
    for i in range(_,len(A),a):
        ans.append(A[i])
        j=i+a-2*_
        if(_!=0 and _!=B-1 and j<len(A)):
            ans.append(A[j])

print(''.join(ans))