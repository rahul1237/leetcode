A=8
ans=[]
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        ans.append(str(num%2))
    return ans
a=DecimalToBinary(A)
# print(a)
a.reverse()
count=0
for _ in a:
    if(_=='1'):
        break
    else:
        count+=1
print(count)