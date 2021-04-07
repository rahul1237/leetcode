A="hello world"

ans=0
a=len(A)

while(a>0):
    a-=1
    if(A[a]!=' '):
        ans+=1
    elif(ans>0): print(ans)

print(ans)
# while(a>=0 and A[a-1]==' '):
#     a-=1

# while(a>=0 and A[a-1]!=' '):
#     a-=1
#     ans+=1

# print(ans)