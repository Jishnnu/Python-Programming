"""
Write a python program to reverse a given number using while loop.

"""

number = int(input("ENTER A NUMBER : "))

if len(str(number)) == 1:
    print("AS THE NUMBER ONLY HAS A SINGLE DIGIT, THE REVERSE IS THE SAME AS INPUT :", number)

else:
    rem, rev = 0, 0    
    while number > 0:
        rem = number % 10
        rev = (rev * 10) + rem
        number //= 10

    print("REVERSED NUMBER :", rev)