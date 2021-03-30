s=input()
s=s.lower()
b=[_ for _ in s if _.isalnum()]

c1=list(''.join(b))
c2=list(''.join(b))
c1.reverse()
print(''.join(c1))
print(''.join(c2))
if(c1==c2):
    print(True)
else:
    print(False)
