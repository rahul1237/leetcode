A=5

if(A>1):
    for _ in range(2,int(A**0.5)):
        if(A%_==0):
           print(0)

    print(1)
else:
    print(0)