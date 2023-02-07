"""
Write a python program which accepts a sequence of comma separated numbers from user and generate a list  
and tuple with those numbers.

"""

numbers = input("\nENTER A SEQUENCE OF COMMA SEPARATED NUMBERS : ")
list = numbers.split(',')
tuple = tuple(list)

print("LIST :", list)
print("TUPLE :", tuple)
