A='ABEC'
A=A.lower()

ans=0

for _ in range(len(A)):
    if(A[_]=='a' or A[_]=='e' or A[_]=='i' or A[_]=='o' or A[_]=='u'):
        ans+=len(A)-_

print(ans%10003)