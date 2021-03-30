n=int(input())

a=str(n)

sum=0
prod=1

for _ in range(len(a)):
    sum+=int(a[_])
    prod*=int(a[_])

print(abs(prod-sum))