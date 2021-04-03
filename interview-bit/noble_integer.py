A=[5,6,2]
flag=0
for _ in range(len(A)):
    count=[]
    temp=A[_]
    for i in A:
        if(i>A[_]):
            count.append(i)
    
    # print(A[_],len(count))

    if(A[_]==len(count)):
        flag=1
        break
    # break
if(flag==1):
    print(1)
else:
    print(-1)