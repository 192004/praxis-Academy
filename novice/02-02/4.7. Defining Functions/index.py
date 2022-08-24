def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a+b
    print()

fib(10)
print(fib)

f=fib
f(100)
print(fib)

fib(0)
print(fib(0))

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

    f1000 = fib2(100)
    print (f1000)
