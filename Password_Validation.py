"""
Read a password from user. It is valid only if it starts with a character, contains an underscore and 
ends with a numerical. Write a python program to validate the password.

"""

flag = 0
password = input("\nENTER YOUR PASSWORD (STARTS WITH CHARACTER, ENDS WITH NUMBER & SHOULD HAVE AN UNDERSCORE) : ")

if len(password) <= 5:
    print("INVALID ENTRY. PASSWORD SHOULD HAVE ATLEAST 6 CHARACTERS")
    quit()

if password[0].islower() or password[0].isupper():
    if password[len(password) - 1].isdigit():
        for i in password:    
            if i == '_':                
                flag = 1
                break                                    
    else:
        print("ERROR : PASSWORD SHOULD END WITH A NUMBER")
        quit()

else:
    print("ERROR : PASSWORD SHOULD BEGIN WITH A CHARACTER")

if flag == 1:
    print("SUCCESS : PASSWORD IS VALID AND STRONG\n")

else:
    print("ERROR : PASSWORD DOESN'T HAVE AN UNDERSCORE")                
