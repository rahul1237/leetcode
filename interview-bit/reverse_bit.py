A=3
a=('{:032b}'.format(A))
b=list(a)
# print(a)
b.reverse()
c=''.join(b)
# print(c)
print(int(c,2))
# print(list(a))
# ans=0
# def binaryToDecimal(n):
#     num = n
#     dec_value = 0
#     base = 1
     
#     temp = num
#     while(temp):
#         last_digit = temp % 10
#         temp = int(temp / 10)
         
#         dec_value += last_digit * base
#         base = base * 2
#     return dec_value

# print(binaryToDecimal(int(c)))