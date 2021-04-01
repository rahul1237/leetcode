A=4

def fact(A):
    if(A==1):
        return A
    else:
        return A*fact(A-1)

ans=str(fact(A))
anss=list(ans)
anss.reverse()
new=int(''.join(anss))


print(abs(len(str(new))-len(ans)))