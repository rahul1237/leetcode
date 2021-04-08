A=3
ans=[]
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        ans.append(str(num%2))
    return ''.join(ans)
a=DecimalToBinary(A)
# a=str(A).strip('0')
print(a.count('1'))