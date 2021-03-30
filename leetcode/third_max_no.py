nums=list(map(int,input().split()))

a=set(nums)

b=sorted(list(a))

if(len(b) < 3):
    print(max(b))
else:
    print(b[-3])