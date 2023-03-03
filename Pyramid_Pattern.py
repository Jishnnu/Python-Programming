"""
Write a program that prints the following pyramid on the screen.
1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5

"""

print("PYRAMID PATTERN :")
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1    
    print("")
    i += 1
