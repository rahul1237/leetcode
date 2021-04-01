A=44729790
a=str(A)
b=list(a)
b.reverse()

if(A<-2147483648 or A>2147483647):
    print(0)
elif(A>0):
    if(int(''.join(b))>2147483647):
        print(0)
    else:
        print(int(''.join(b)))
else:
    b.remove('-')
    x=int(''.join(b))*-1
    if(x<-2147483648):
        print(0)
    else:
        print(x)
