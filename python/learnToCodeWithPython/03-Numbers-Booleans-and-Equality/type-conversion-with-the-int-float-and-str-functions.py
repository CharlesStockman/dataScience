# How do I convert the string “1000” to an integer? Write your code below.
print(int("1000"))
print(type(int("1000")))

# How do I convert the floating point number 3.764 to an integer? 
print(int(3.764))
print(type(int(3.764)))

# In a Python program, I have my business expenses represented by a floating point number: 99.45.

# I want to express this value as a string. However, I also want to add a dollar sign "$" in front of the amount a
# space and the word “dollars” at the end.  The final result should be "$99.45 dollars".
print("$", str(99.45), " dollars")

#
# Provide some example of converting a datatype into another datatype
#
print("Boolean Converted to String      ", str(True))
print("String  Converted to Boolean     ", bool("True"))
print("Int     Converted to Boolean     ", bool(0))
print("Integer Converted to String      ", str(3))
print("String  Converted to Integer     ", int(3))
print("Float   Converted to String      ", str(3.45))
print("String  Converted to Float       ", float("3.45"))
