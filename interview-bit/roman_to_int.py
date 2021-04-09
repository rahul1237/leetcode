A='XX'

a={
    'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
}

ans=0
cu=0
pr=0

for _ in range(len(A)):
    cu=a[A[_]]
    if(cu>pr):
        ans+=cu-2*pr
    else:
        ans+=cu
    pr=cu

print(ans)