moves=input()

x,y=0,0

for _ in moves:
    if(_=='L'):
        x-=1
    elif(_=='R'):
        x+=1
    elif(_=='U'):
        y+=1
    else:
        y-=1

if(x==0 and y==0):
    print(True)
else:
    print(False)