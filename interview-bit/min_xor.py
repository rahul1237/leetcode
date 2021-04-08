A=[0, 2, 5, 7]

a=10000000

A=sorted(A)
for _ in range(len(A)-1):
    if(A[_]^A[_+1] < a):
        a=A[_]^A[_+1]
print(a)