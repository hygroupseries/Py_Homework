# fib.py 斐波那契数列
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)

for i in range(1,100):
    print(fib(i))