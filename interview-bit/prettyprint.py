A=3

ans=[]
n=2+A-1
m=A-1
for _ in range(n):
    for i in range(n):
        ans.append([_,i])

n_ans=[]

for _ in ans:
    row=max(abs(_[0]-m),abs(_[1]-m))+1
    n_ans.append(row)

print(n_ans[_:_+n] for _ in range(0,len(n_ans),n))