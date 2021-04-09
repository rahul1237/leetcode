A='()'

if(len(A)%2!=0):
    print(0)
stack=[]
for i in A:
    if(i=="("):
        stack.append("(")
        
    elif(i==")"):
        if stack:
            stack.pop(0)
            

if(A[0]==")"):
    print(0)

if(stack==[]):
    print(1)
else:
    print(0)