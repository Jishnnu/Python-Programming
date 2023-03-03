"""
A file has the database of employee. Each record is of 30 characters, with fields like 
empID, empName, mark1, mark2 and mark3. Read the file content from 2nd record.

"""
file_handler = open("C:/Users/jishn/Documents/Programming/Python/File_Handling/Employee_Records/Dataset.txt")
record = file_handler.readlines()
print("\nSECOND RECORD :")
print(record[1])


