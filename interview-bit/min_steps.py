A=[-7,-13]
B=[1,-5]

step=0

for _ in range(len(A)-1):
    x=abs(A[_]-A[_+1])
    y=abs(B[_]-B[_+1])

    step+=min(x,y)

    step+=(max(x,y)-min(x,y))


print(step)