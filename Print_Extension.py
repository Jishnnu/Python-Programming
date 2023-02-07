""" 
Write a python program to accept a filename from the user and print its extension.
Input: word.doc
Output: doc

"""

filename = input("\nENTER FILENAME WITH EXENSION : ")
filename_new = filename.split(".")
print("FILE EXTENSION :", filename_new[-1])
