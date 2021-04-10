A=[1]

    
one_exists = False
n = len(A)
for i in range(n):
    if A[i] == 1:
        one_exists = True
    if A[i] > n or A[i] < 1:
        A[i] = 1

if not one_exists:
    print(1)

for i in range(n):
    pos = abs(A[i]) - 1
    if A[pos] > 0:
        A[pos] *= -1

for i in range(n):
    if A[i] > 0:
        print(i+1)

print(n+1)