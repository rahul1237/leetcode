A=[1,2,3]

a=[]

for _ in A:
    a.append(str(_))

a=int(''.join(a))

ans=[]

a+=1

a=str(a)

for _ in range(len(a)):
    ans.append(int(a[_]))

print(ans)