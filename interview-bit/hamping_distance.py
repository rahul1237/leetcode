A=[2,4,6]

ans=0

for _ in range(32):
    count=0
    for i in range(len(A)):
        if(A[i]&(1<<_)):
            count+=1
    ans+=count*(len(A)-count)*2


print(ans%1000000007)