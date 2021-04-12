A="(a + (a + b))"

stack=[]
ops=['+','*','/','-']

for i in A:
    if i=='(':
        stack.append(i)
    if i in ops and stack:
        stack.pop()
        
if not stack:
    print(0)
else:
    print(1)