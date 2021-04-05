A=30
B=12
import math
while(math.gcd(A,B)!=1):
    A//=math.gcd(A,B)
print(A)