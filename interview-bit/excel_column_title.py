A=27

max=50

a=['\0']*max

_=0

while(A>0):
    r=A%26

    if(r==0):
        a[_]='Z'
        _+=1
        A=(A//26)-1
    else:
        a[_]=chr((r-1)+ord('A'))
        _+=1
        A//=26

# a[_]='/0'

a=a[::-1]
print(''.join(a))