"""
Write a python program to find the factorial of a number.

"""

n = int(input("ENTER A DIGIT : "))

i = factorial = 1
while i <= n:
    factorial *= i
    i += 1

print(f"FACTORIAL OF {n} = {factorial}")
