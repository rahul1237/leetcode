from math import factorial
A=5
n = A+1
ans=[]
for i in range(n):
    row=[]
    for j in range(i+1):
        row.append(factorial(i)//(factorial(j)*factorial(i-j)))
    

    ans.append(row)

print(ans)
print(ans[A])