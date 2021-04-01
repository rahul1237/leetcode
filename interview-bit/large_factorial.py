def fact(A):
    ans=1
    if(A==0):
        return 1
    else:
        for _ in range(1,A+1):
            ans=ans*_

        return ans

print(fact(6))