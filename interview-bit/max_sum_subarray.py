A=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

sum=0
ansarr=[]

for _ in range(len(A)):
    sum+=A[_]
    ansarr.append(max(sum,A[_]))
    if(sum<0):
        sum=0

print(max(ansarr))