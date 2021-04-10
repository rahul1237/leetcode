for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=list(set(b))
    ans=0
    if(b.count(c[0])>1):
        ans=c[1]
    else:
        ans=c[0]
    print(b.index(ans)+1)

