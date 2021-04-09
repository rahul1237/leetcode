A='1e10'
try:
    x=float(A)
    y=A.split('e')
    for ele in y:
        if ele=="":
            print(0)
        if ele[-1]==".":
            print(0)

    print(1)
        
except:
    print(0)