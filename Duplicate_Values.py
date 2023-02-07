"""
Read a string and find the number of unique characters in it and remove the duplicate characters.

"""

string = input("\nENTER A STRING : ")

set_string = set(string)
print("UNIQUE CHARACTERS :", set_string)
print("LENGTH OF UNIQUE CHARACTERS' LIST :", len(set_string))

list_string = list(string)
for element in set_string:
    list_string.remove(element)

print("REPEATED CHARACTERS : ", set(list_string))
