A=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

a=len(A)
ans=[]

# upper t
for _ in range(a):
    col=_
    row=0
    mid=[]

    while(col>=0):
        mid.append(A[row][col])
        row+=1
        col-=1

    ans.append(mid)

# lower t

for _ in range(1,a):
    col=a-1
    row=_
    mid=[]
    while(row<a):
        mid.append(A[row][col])
        row+=1
        col-=1
    
    ans.append(mid)

print(ans)