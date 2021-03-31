A=[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
column = len(A[0])
row = len(A)

top=0
left=0
bottom=row-1
right=column-1

movement=0

ans=[]

while(top<=bottom and left<=right):
    if(movement==0):
        for _ in range(left,right+1):
            ans.append(A[top][_])
        top+=1
        movement=1
    elif(movement==1):
        for _ in range(top,bottom+1):
            ans.append(A[_][right])
        right-=1
        movement=2
    elif(movement==2):
        for _ in range(right,left-1,-1):
            ans.append(A[bottom][_])
        bottom-=1
        movement=3
    elif(movement==3):
        for _ in range(bottom,top-1,-1):
            ans.append(A[_][left])
        left+=1
        movement=0

# print(column,row)
print(ans)
# print(A[bottom][right-1])
# print(A[top])