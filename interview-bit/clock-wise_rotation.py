A=[
    [1,2],
    [3,4]
]

for _ in range(len(A)):
    for i in range(_,len(A)):
        A[_][i],A[i][_]=A[i][_],A[_][i]

for _ in range(len(A)):
    for i in range(len(A)//2):
        A[_][i],A[_][len(A)-i-1]=A[_][len(A)-i-1],A[_][i]

print(A)