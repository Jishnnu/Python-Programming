"""
Write a program to print the quotient and remainder of two values taken as input from the user. 
Use Exception Handling to deal with common exceptions in the context of this program.

"""

try:
  numerator = int(input("ENTER NUMERATOR : "))
  denominator = int(input("ENTER DENOMINATOR : "))
  quotient = numerator / denominator
  remainder = numerator % denominator

except (ValueError, ZeroDivisionError, TypeError, NameError, KeyboardInterrupt) as e:
  print("\nEXCEPTION OCCURRED :\nDESCRIPTION :", e)

except:
  print("\nUNEXPECTED EXCEPTION OCCURRED")

else:
  print("\nQUOTIENT :", quotient)
  print("REMAINDER :", remainder)

finally:
  print("\n------------- END OF PROGRAM -------------\n")