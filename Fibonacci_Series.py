"""
Write a python program to generate Fibonacci series of 5 terms.

"""
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("\nENTER A DIGIT : "))

if num < 0:
    print("FIBONACCI SERIES ACCEPTS NON-ZERO INPUTS ONLY")
    quit()

print("FIBONACCI SERIES :")
for i in range(num):
    if fibonacci(i) != -1:
        print(fibonacci(i))


"""
ALTERNATIVE METHOD :

def fib(n):
    if n < 0:
        raise ValuError("Need a non-negative value")
    
    a, b = 0, 1
    L = []
    while len(L) < n:
        a, b = b, a + b
        L.append(a)
    return L
    
print(fib(num))

"""