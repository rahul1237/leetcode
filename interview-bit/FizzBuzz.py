A=5
ans=[]
for _ in range(1,A+1):
    if(_%5==0 and _%3==0):
        ans.append('FizzBuzz')
    elif(_%5==0):
        ans.append('Buzz')
    elif(_%3==0):
        ans.append('Fizz')
    else:
        ans.append(_)

print(ans)