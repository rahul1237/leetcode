A=[0,0,0,0,1]
B=3

if(B>=len(A)):
    print(1)

_,t=0,0
ans=0
while(_<len(A)):
    flag=0
    for j in range(_+B-1,t+1,-1):
        if(A[j]==1):
            t=j+1
            flag=1
            ans+=1
            _=j+B
            break


if(_>=len(A)):
    print(ans)
if(flag==0):
    print(-1)
