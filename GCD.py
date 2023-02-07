"""
Write a python program to find the GCD of two numbers using for loop.

"""

def GCD(num1, num2):
    hcf = min(num1, num2)
 
    while hcf:
        if num1 % hcf == 0 and num2 % hcf == 0:
            break
        hcf -= 1
 
    # Return the gcd of a and b
    return hcf

n1 = int(input("\nENTER A NUMBER : "))
n2 = int(input("ENTER ANOTHER NUMBER : "))

print(f"GCD({n1}, {n2}) = {GCD(n1, n2)}")

