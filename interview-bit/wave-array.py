A=[5,10,6,7,9,12,14]

B=sorted(A)

for _ in range(len(A)):
    if(_%2!=0):
        temp=B[_-1]
        B[_-1]=B[_]
        B[_]=temp
    
print(B)