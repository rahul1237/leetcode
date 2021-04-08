A=")("

ans=0
a=[]

for _ in range(len(A)):
    if(A[_]=='('):
        a.append(A[_])
    if(A[_]==')'):
        if(len(a)==0):
            ans+=1
        else:
            a.pop()
    

print(ans+len(a))