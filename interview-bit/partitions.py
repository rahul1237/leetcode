A=9
B=[ 0, 0, 0, 0, 0, 0,0,0,0]
nB=[]
for _ in B:
    nB.append(_)
B_sum=sum(B)
dup=[]
for _ in range(B.count(B_sum//3)):
    ind=B.index(B_sum//3)
    if(ind in dup):
        pass
    else:
        B[ind]='A'
        dup.append(ind)
print(set(nB))

if(B_sum==0 and 0 in set(nB) and len(set(nB))==1 ):
    print((A*3)+1)
    # print(set(nB))
    # print(2)
elif(B_sum%3!=0):
    print(0)
else:
    zero=0
    for _ in dup:
        if(_==len(nB)-1):
            pass
        
        elif(nB[_+1]==0):
            zero+=1
    if(zero==0):
        print(1)
    else:
        print(zero*2)


# #     if(0 in B):
# #         print((B.count(0)*2))
# #     else:
# #         print(1)

# print(B_sum)
# print(B_sum//3)
# print(B.count(B_sum//3))
# print(dup)
# print(B)
#     # if sum//3!0 then return 0
