A='AAA'
ans=0
for _ in range(len(A)):
    ans*=26
    ans+=ord(A[_]) - ord('A') + 1

print(ans)