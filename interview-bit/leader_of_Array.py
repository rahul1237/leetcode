A=[16, 17, 4, 3, 5, 2]

ans=[]

for _ in range(len(A)):
    max_list=[]
    for i in range(A.index(A[_])+1,len(A)):
        max_list.append(A[i])
    if(len(max_list)!=0):
        max_right=max(max_list)
    if(A[_]>max_right):
        ans.append(A[_])
ans.append(A[len(A)-1])
print(ans)