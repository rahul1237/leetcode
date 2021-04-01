A=2
B=3
C=2
D=2

arr=[A,B,C,D]
ans=0
if(len(set(arr))==2):
    for _ in set(arr):
        if(arr.count(_)==2):
            ans+=1
    if(ans==2):
        print(1)
    else:
        print(0)
else:
    print(0)