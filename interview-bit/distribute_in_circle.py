A=8
B=5
C=2

if(A<=B-C+1):
    print(A+C-1)
else:
    A=A-(B-C+1)

    if(A%B)==0:
        print(B)
    else:
        print(A%B)