"""
Illustrate exception handling for Divide by zero error.

"""

try:
  numerator = int(input("\nENTER NUMERATOR : "))
  denominator = int(input("ENTER DENOMINATOR : "))
  quotient = numerator / denominator
  remainder = numerator % denominator

except ZeroDivisionError as e:
  print("\nEXCEPTION OCCURRED :\nDESCRIPTION :", e)

except:
  print("\nUNEXPECTED EXCEPTION OCCURRED")

else:
  print("\nQUOTIENT :", quotient)
  print("REMAINDER :", remainder)

finally:
  print("\n------------- END OF PROGRAM -------------\n")