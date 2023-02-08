"""
Write a python program to write to a file the string read from the user. Display the file content.

"""

# READING A STRING INPUT
string_1 = input("\nENTER A STRING : ")

# FILE HANDLING - WRITE OPERATION
file_handler = open("StringRead.txt", "w")
print("\nFILE POINTER POSITION : ", file_handler.tell())
file_handler.write(string_1)
file_handler.close()

# READING ANOTHER STRING INPUT
string_2 = input("\nENTER ANOTHER STRING : ")

# FILE HANDLING - APPEND OPERATION
file_handler = open("StringRead.txt", "a")
print("\nFILE POINTER POSITION : ", file_handler.tell())
file_handler.write(string_2)
file_handler.close()

# FILE HANDLING - READ OPERATION
file_handler = open("StringRead.txt", "r")
output = file_handler.read()
file_handler.close()
print("\nCONTENTS IN THE FILE :\n", output)

# READING ANOTHER STRING INPUT
string_3 = input("\nENTER ANOTHER STRING : ")

# FILE HANDLING - READ OPERATION ON APPEND +
file_handler = open("StringRead.txt", "a+")
file_handler.write(string_3)
print("\nFILE POINTER POSITION : ", file_handler.tell())
file_handler.close()

# FILE HANDLING - READ OPERATION
file_handler = open("StringRead.txt", "r")
file_handler.seek(5, 0)
output = file_handler.read()
print("\nCONTENTS IN THE FILE FROM POSITION '5' :\n", output)
print("\nFILE POINTER POSITION : ", file_handler.tell())
file_handler.close()