A=[5, -2, 3 , 1, 2]
B=3

Sum = Max = sum(A[:B])
N = len(A)
for b in range(1, B+1):
    Sum = Sum - A[B - b] + A[N - b]
    if Sum > Max:
        Max = Sum
print(Max)