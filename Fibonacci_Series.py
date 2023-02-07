"""
Write a python program to generate Fibonacci series of 5 terms.

"""

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("\nENTER A DIGIT : "))

print("FIBONACCI SERIES :")
for i in range(num):
    print(fibonacci(i))