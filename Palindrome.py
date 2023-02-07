"""
Write a python program to check whether a given number is palindrome or not using a python program.

"""
number = int(input("\nENTER A NUMBER : "))

if len(str(number)) == 1:
    print("THE NUMBER", number,"ONLY HAS A SINGLE DIGIT")

else:
    rem, rev, temp = 0, 0, number
    while temp > 0:
        rem = temp % 10
        rev = (rev * 10) + rem
        temp //= 10

    if number == rev:
        print(number, "IS A PALINDROME")

    else:
        print(number, "IS NOT A PALINDROME")