# Factorial
def fact(n):
    if n==0: return 1
    else: return n*fact(n-1)

print(fact(5))

# Fibonacci Sequence 1,1,2,3,5,8,13
def fib(r):
    if r==1: return 1
    elif r==2: return 1
    else: return fib(r-1)+fib(r-2)

print(fib(7))
