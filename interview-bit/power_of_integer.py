A=4

if(A==1):
    print(True)

else:
    for _ in range(2,int((A**0.5)+1)):
        a=2
        b=int(_**a)

        while(b<=A and b>0):
            if(b==A):
                print(True)
            else:
                a+=1
                b=_**a
            break
    print(False)