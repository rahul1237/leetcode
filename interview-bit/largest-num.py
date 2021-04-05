A=[3, 30, 34, 9, 5]

a=[]

for _ in A:
    a.append(str(_))

b=sorted(a)
b.reverse()
print(''.join(b))