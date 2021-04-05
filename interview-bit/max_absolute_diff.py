A=[1,3,-1]

ma1=-100000000
ma2=-100000000
mi1=100000000
mi2=100000000


for _ in range(len(A)):
    ma1=max(ma1,A[_]+_)
    ma2=max(ma2,A[_]+_)

    mi1=min(mi1,A[_]+_)
    mi2=min(mi2,A[_]+_)

print(max(ma1-mi1,ma2-mi2))