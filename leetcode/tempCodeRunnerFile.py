s=input()

b=''

for _ in s:
    if(s.isalnum()):
        b+=_

c1=list(''.join(b))
c2=list(''.join(b))
c1.reverse()

if(c1==c2):
    print(True)
else:
    print(False)
