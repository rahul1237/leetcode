def fib(A):
    if(A==1):
        return 1
    elif(A==2):
        return 1
    else:
        return fib(A-1)+fib(A-2)

print(fib(3))