# a,b=map(int,input().split())
# b=list(map(int,input().split()))
# c=list(map(int,input().split()))

# dic={}

# for _ in set(b):
#     dic[_]=b.index(_)+1

# ans=[]

# for _ in c:
#     ans.append(str(dic[_]))
#     for i in range(1,len(dic)+1):
#         if(dic[i]<dic[_]):
#             dic[i]+=1 
#     dic[_]=1

# print(' '.join(ans))

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    x=['1']
    y=['1']
    for _ in range(a-1):
        x.append('0')
    for _ in range(b-1):
        y.append('0')
    if(a<=b):
        y[-c]='1'
    else:
        x[-c]='1'
    print(''.join(x),''.join(y))