A="A man, a plan, a canal: Panama"
A=A.lower()
a=''
for _ in range(len(A)):
    # if(A[_]==' '):
    #     pass
    if(A[_].isalnum()):
        a+=A[_]

b=a[::-1]

if(b==a):
    print(1)
else:
    print(0)

# print(a)
# print(b)