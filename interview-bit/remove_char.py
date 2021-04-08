A='aaabaa'
B=2
a=0
b=0
ans=''

while(a<len(A)):
    b=a
    while(A[b]==A[b+1] and b<len(A)):
        b+=1
    if(b-a+1!=B):
        ans+=A[a:b-a+1]
        a=b+1

print(ans)